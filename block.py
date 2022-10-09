from datetime import datetime
from gettext import translation
import hashlib
from transaction import Transaction
from wallet import Wallet
from merkle import MerkleTree




class Block:
    def __init__(self, date, transactionhash, transaction_list = None, prev_hash=None):
        self.__date = date
        self.transaction_list = transaction_list
        self.__transactionhash = self.get_mtreenode()
        #self.__transactionhash = transactionhash
        self.__prev_hash = prev_hash
        self.__series = 0
        self.__nonce = 0
        self.__hash = self.calculate_hash()
        
    def get_mtreenode(self):
        if self.transaction_list is None:
            return "Genesis"
        
        hash_list = []
        for transaction in self.transaction_list:
            hash_list.append(transaction.transaction_hash)
        mtree = MerkleTree(hash_list)
        return mtree.getRootHash()

    def calculate_hash(self):
        date = str(self.__date).encode()
        transactionhash = str(self.__transactionhash).encode()
        prev_hash = self.__prev_hash.hexdigest().encode() if self.__prev_hash else str(None).encode()
        nonce = str(self.__nonce).encode()
        return hashlib.sha256(date + transactionhash + prev_hash + nonce)

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

    def get_series(self):
        return self.__series
    def set_series(self, series):
        self.__series = series

    # Only for test
    def change_block_data(self, to_wallet, amount):
        #Itt meg folytatni kene
        self.transaction_list[0].hack_transaction(to_wallet, amount)
        self.__transactionhash = self.transaction_list[0].transaction_hash 
        self.__hash = self.calculate_hash()

    def __str__(self):
        if self.__prev_hash is None:
            return f"Series: {self.__series};\nBlock: {self.get_hash().hexdigest()};\nTransaction Hash: {self.__transactionhash};\nPrevious hash: {None};\nNonce: {self.__nonce};"
        return f"Series: {self.__series};\nBlock: {self.get_hash().hexdigest()};\nTransaction Hash: {self.__transactionhash};\nPrevious hash: {self.get_prev_hash().hexdigest()}"

    def show_transactions(self):
        if self.transaction_list is None:
            print("Genesis transaction")
        else:
            for transaction in self.transaction_list:
                print(transaction)

        



if __name__ == "__main__":
    
    bob_wallet = Wallet("Bob")
    jack_wallet = Wallet("Jack")
    transaction1 = Transaction(bob_wallet, jack_wallet, 10)
    transaction2 = Transaction(jack_wallet, bob_wallet, 10)
    transaction3 = Transaction(jack_wallet, bob_wallet, 15)

    b1 = Block(date = datetime.now(), transactionhash = transaction1.transaction_hash, transaction_list=[transaction1])
    b2 = Block(date = datetime.now(), transactionhash = transaction2.transaction_hash, transaction_list=[transaction2], prev_hash = b1.get_hash())
    b2.set_series(1)
    b3 = Block(date = datetime.now(), transactionhash = transaction3.transaction_hash, transaction_list=[transaction3], prev_hash = b2.get_hash())
    b3.set_series(2)
    print(b1)
    print(b2)
    print(b3)

    hacker_wallet = Wallet("Hacker")
    print("*"*30)
    b2.change_block_data(hacker_wallet, 20)
    print(b2)


    print("*"*30)
    print(b3.get_mtreenode())