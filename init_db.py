from sqlalchemy import create_engine

from infrastructure.sqlalchemy_repositories import VoteBase
from config import DatabaseConfig

engine = create_engine(DatabaseConfig.DATABASE_URL)

VoteBase.metadata.create_all(bind=engine)
