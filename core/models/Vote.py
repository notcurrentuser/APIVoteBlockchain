from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Vote:
    voter_id: str
    candidate_id: str
    timestamp: datetime
    blockchain_tx_hash: Optional[str] = None
