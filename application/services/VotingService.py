from core.models import Vote
from core.repositories import VoteRepository
from datetime import datetime
from web3 import Web3
from web3.gas_strategies.time_based import slow_gas_price_strategy


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
        _votes = self.repository.get_votes()
        _votes.reverse()
        return _votes

    def _record_to_blockchain(self, vote: Vote) -> str:
        # Функція для запису в блокчейн
        tx = {
            'to': '0xB2c0A791F886a210d49bb57c098243342a2cE62b',
            'value': int(self.blockchain.to_wei(0.000001, 'ether')),
            'gas': 300000,
            'gasPrice': self.blockchain.to_wei('5', 'gwei'),
            'nonce': self.blockchain.eth.get_transaction_count(self.blockchain.eth.default_account),
            'data': str.encode(f"Voter: {vote.voter_id}, Candidate: {vote.candidate_id}"),
            'chainId': self.blockchain.eth.chain_id
        }

        signed_tx = self.blockchain.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.blockchain.eth.send_raw_transaction(signed_tx.raw_transaction)
        return self.blockchain.to_hex(tx_hash)
