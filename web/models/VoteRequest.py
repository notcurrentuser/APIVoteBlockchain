from pydantic import BaseModel


class VoteRequest(BaseModel):
    voter_id: str
    candidate_id: str
