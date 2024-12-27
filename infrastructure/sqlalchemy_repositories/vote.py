from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from core.models import Vote
from core.repositories import VoteRepository

Base = declarative_base()


class VoteModel(Base):
    __tablename__ = "votes"
    voter_id = Column(String, primary_key=True)
    candidate_id = Column(String)
    timestamp = Column(DateTime)
    blockchain_tx_hash = Column(String)


class SQLAlchemyVoteRepository(VoteRepository):
    def __init__(self, session):
        self.session = session

    def save(self, vote: Vote) -> None:
        vote_model = VoteModel(
            voter_id=vote.voter_id,
            candidate_id=vote.candidate_id,
            timestamp=vote.timestamp,
            blockchain_tx_hash=vote.blockchain_tx_hash
        )
        self.session.add(vote_model)
        self.session.commit()

    def get_votes(self):
        return [
            Vote(
                voter_id=row.voter_id,
                candidate_id=row.candidate_id,
                timestamp=row.timestamp,
                blockchain_tx_hash=row.blockchain_tx_hash
            )
            for row in self.session.query(VoteModel).all()
        ]
