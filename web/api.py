from models import VoteRequest
from base import app, service
from fastapi import HTTPException


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
