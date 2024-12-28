from core.models import Vote
from core.repositories import VoteRepository
from datetime import datetime
from web3 import Web3


class VotingService:
    def __init__(self, repository: VoteRepository, blockchain: Web3, contract_address: str, private_key: str):
        self.repository = repository
        self.blockchain = blockchain
        self.contract_address = contract_address
        self.private_key = private_key

    def submit_vote(self, voter_id: str, candidate_id: str) -> Vote:
        vote = Vote(
            voter_id=voter_id,
            candidate_id=candidate_id,
            timestamp=datetime.now()
        )

        # Запис голосу у блокчейн
        tx_hash = self._record_to_blockchain(vote)
        vote.blockchain_tx_hash = tx_hash

        # Збереження голосу в базі даних
        self.repository.save(vote)
        return vote

    def get_votes(self):
        return self.repository.get_votes()

    def _record_to_blockchain(self, vote: Vote) -> str:
        # Функція для запису в блокчейн
        tx = {
            'to': self.contract_address,
            'value': 0,
            'gas': 2000000,
            'gasPrice': self.blockchain.to_wei('50', 'gwei'),
            'nonce': self.blockchain.eth.get_transaction_count(self.blockchain.eth.default_account),
            'data': str.encode(f"Voter: {vote.voter_id}, Candidate: {vote.candidate_id}")
        }
        signed_tx = self.blockchain.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.blockchain.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.blockchain.to_hex(tx_hash)
