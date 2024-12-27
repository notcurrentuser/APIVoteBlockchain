from sqlalchemy import create_engine
from infrastructure.sqlalchemy_repositories import VoteBase

DATABASE_URL = "sqlite:///./votes.db"
engine = create_engine(DATABASE_URL)

VoteBase.metadata.create_all(bind=engine)
