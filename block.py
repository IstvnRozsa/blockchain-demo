from datetime import datetime
from gettext import translation
import hashlib
from transaction import Transaction
from wallet import Wallet




class Block:
    def __init__(self, date, transactions, prev_hash=None):
        self.__date = date
        self.__transactions = transactions
        self.__prev_hash = prev_hash
        self.__nonce = 0
        self.__hash = self.calculate_hash()
        
        

    def calculate_hash(self):
        date = str(self.__date).encode()
        transactions = str(self.__transactions).encode()
        prev_hash = self.__prev_hash.hexdigest().encode() if self.__prev_hash else str(None).encode()
        nonce = str(self.__nonce).encode()
        return hashlib.sha256(date + transactions + prev_hash + nonce)

    def mine_block(self, difficulty):
        while self.__hash.hexdigest()[0:difficulty] != "0" * difficulty:
            self.__nonce += 1
            self.__hash = self.calculate_hash()



    def get_hash(self):
        return self.__hash
    
    def get_prev_hash(self):
        return self.__prev_hash

    def set_prev_hash(self, _hash):
        self.__prev_hash = _hash

    # Only for test
    def change_block_data(self):
        self.__transactions = Transaction("Bob", "Bob", 100000)

    def __str__(self):
        if self.__prev_hash is None:
            return f"Block: {self.get_hash().hexdigest()}; Transactions: {self.__transactions}; Previous hash: {None}"
        return f"Block: {self.get_hash().hexdigest()}; Transactions: {self.__transactions}; Previous hash: {self.get_prev_hash().hexdigest()}"
        



if __name__ == "__main__":
    
    bob_wallet = Wallet("Bob")
    jack_wallet = Wallet("Jack")
    transaction1 = Transaction(bob_wallet, jack_wallet, 10)
    transaction2 = Transaction(jack_wallet, bob_wallet, 10)
    transaction3 = Transaction(jack_wallet, bob_wallet, 15)

    b1 = Block(date = datetime.now(), transactions = transaction1.transaction_hash)
    b2 = Block(date = datetime.now(), transactions = transaction2.transaction_hash, prev_hash = b1.get_hash())
    b3 = Block(date = datetime.now(),transactions= transaction3.transaction_hash, prev_hash =  b2.get_hash())
    print(b1)
    print(b2)
    print(b3)