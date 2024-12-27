from abc import ABC, abstractmethod
from typing import List
from core.models import Vote


class VoteRepository(ABC):
    @abstractmethod
    def save(self, vote: Vote) -> None:
        pass

    @abstractmethod
    def get_votes(self) -> List[Vote]:
        pass
