class BlockchainConfig:
    TO_ADDRESS: str = '0xB2c0A791F886a210d49bb57c098243342a2cE62b'

    GAS_NUMBER: int = 300000
    GAS_PRICE: str = '5'

    BLOCKCHAIN_URL = "https://bscrpc.com"
    CONTACT_ADDRESS = "0x0000000000000000000000000000000000000000"

    # test
    PRIVATE_KEY = "adf114dd49ec1b15873352a7527532557a0e4b0d92dcd730621bf62884b141fc"


class DatabaseConfig:
    DATABASE_URL = "sqlite:///./votes.db"
