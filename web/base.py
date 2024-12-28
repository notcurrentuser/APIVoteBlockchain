from fastapi import FastAPI
from fastapi import HTTPException
from application.services import VotingService
from infrastructure.sqlalchemy_repositories import SQLAlchemyVoteRepository
from .models import VoteRequest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from web3 import Web3

# Ініціалізація FastAPI
app = FastAPI()

# База даних
DATABASE_URL = "sqlite:///./votes.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Блокчейн
BLOCKCHAIN_URL = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(BLOCKCHAIN_URL))
# web3.eth.default_account = web3.eth.accounts[0]

# Ініціалізація сервісу голосування
repository = SQLAlchemyVoteRepository(session)
service = VotingService(
    repository=repository,
    blockchain=web3,
    contract_address="0xxxx",
    private_key="xxxx"
)



@app.post("/vote")
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


@app.get("/votes")
def get_votes():
    return service.get_votes()
