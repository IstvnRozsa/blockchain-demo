from datetime import datetime
from gettext import translation
import hashlib
from transaction import Transaction



class Block:
    def __init__(self, date, transactions, prev_hash=None):
        self.__date = date
        self.__transactions = transactions
        self.__prev_hash = prev_hash
        self.__hash = self.calculate_hash()
        

    def calculate_hash(self):
        date = str(self.__date).encode()
        transactions = str(self.__transactions).encode()
        prev_hash = self.__prev_hash.hexdigest().encode() if self.__prev_hash else str(None).encode()
        return hashlib.sha256(date + transactions + prev_hash)

    def get_hash(self):
        return self.__hash
    
    def get_prev_hash(self):
        return self.__prev_hash

    def __str__(self):
        if self.__prev_hash is None:
            return f"Block: {self.get_hash().hexdigest()}; Transactions: {self.__transactions}; Previous hash: {None}"
        return f"Block: {self.get_hash().hexdigest()}; Transactions: {self.__transactions}; Previous hash: {self.get_prev_hash().hexdigest()}"
        



if __name__ == "__main__":
    b1 = Block(date = datetime.now(), transactions = Transaction(sender="Takasima", receiver="Yakamoto", amount=50))
    b2 = Block(date = datetime.now(), transactions = Transaction(sender="Feri", receiver="Imre", amount=25), prev_hash = b1.get_hash())
    b3 = Block(date = datetime.now(),transactions= Transaction(sender="Timea", receiver="Eniko", amount=25), prev_hash =  b2.get_hash())
    print(b1)
    print(b2)
    print(b3)