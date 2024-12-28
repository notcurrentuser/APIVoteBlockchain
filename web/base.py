from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from web3 import Web3
from web3.gas_strategies.time_based import slow_gas_price_strategy

from application.services import VotingService
from infrastructure.sqlalchemy_repositories import SQLAlchemyVoteRepository
from .models import VoteRequest


# Ініціалізація FastAPI
app = FastAPI()

# База даних
DATABASE_URL = "sqlite:///./votes.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Блокчейн
BLOCKCHAIN_URL = "https://bscrpc.com"
web3 = Web3(Web3.HTTPProvider(BLOCKCHAIN_URL))

PRIVATE_KEY = "adf114dd49ec1b15873352a7527532557a0e4b0d92dcd730621bf62884b141fc"
account = web3.eth.account.from_key(PRIVATE_KEY)
web3.eth.default_account = account.address

balance = web3.eth.get_balance(account.address)
print("Баланс облікового запису:", web3.from_wei(balance, 'ether'))

web3.eth.set_gas_price_strategy(slow_gas_price_strategy)
web3.provider.cache_allowed_requests = True

# Ініціалізація сервісу голосування
repository = SQLAlchemyVoteRepository(session)
service = VotingService(
    repository=repository,
    blockchain=web3,
    contract_address="0x0000000000000000000000000000000000000000",
    private_key=PRIVATE_KEY
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def render_vote_page(request: Request):
    return templates.TemplateResponse("vote.html", {"request": request})

@app.get("/votes", response_class=HTMLResponse)
def render_votes_list(request: Request):
    return templates.TemplateResponse("votes.html", {"request": request, "votes": service.get_votes()})

@app.post("/api/vote")
def submit_vote(vote: VoteRequest):
    try:
        result = service.submit_vote(voter_id=vote.voter_id, candidate_id=vote.candidate_id)
        return {
            "voter_id": result.voter_id,
            "candidate_id": result.candidate_id,
            "timestamp": result.timestamp,
            "blockchain_tx_hash": result.blockchain_tx_hash
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/votes")
def get_votes():
    return service.get_votes()
