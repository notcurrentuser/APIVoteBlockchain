from sqlalchemy import create_engine
from infrastructure.sqlalchemy_repositories.vote import Base

DATABASE_URL = "sqlite:///./votes.db"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)
