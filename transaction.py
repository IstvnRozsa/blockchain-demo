import rsa
import hashlib
from wallet import Wallet



class Transaction:
    def __init__(self, sender:Wallet, receiver:Wallet, amount):
        self.__sender = sender 
        self.__receiver = receiver
        self.__amount = amount
        self.transaction_hash = self.calculate_hash()
        self.signature = rsa.sign(self.transaction_hash.encode(), self.__sender.private_key, "SHA-256")
        

    def calculate_hash(self):
        senderpk = str(self.__sender.public_key).encode()
        receiverpk = str(self.__receiver.public_key).encode()
        amount = str(self.__amount).encode()
        return hashlib.sha256(senderpk + receiverpk + amount).hexdigest()

    def __str__(self) -> str:
        return f"{self.__sender.name} sent {self.__amount} coins to {self.__receiver.name}."
    
    def get_sender(self):
        return self.__sender

    def get_receiver(self):
        return self.__receiver

    def get_amount(self):
        return self.__amount

    def is_valid(self):
        try:
            rsa.verify(self.transaction_hash.encode(), self.signature, self.__sender.public_key)
            return True
        except rsa.VerificationError:
            return False
    
    # Only test
    def hack_transaction(self, wallet, amount:int):
        self.__amount = amount
        self.__receiver = wallet
        self.transaction_hash = self.calculate_hash()



if __name__=="__main__":
    from wallet import Wallet

    bob_wallet = Wallet("Bob")
    jack_wallet = Wallet("Jack")

    transaction = Transaction(bob_wallet, jack_wallet, 10)
    print(transaction)
    print(f"Transaction valid?: {transaction.is_valid()}")

    print("-"*30)
    hacker_wallet = Wallet("Hacker")
    transaction.hack_transaction(hacker_wallet, 100000)
    print(transaction)
    print(f"Transaction valid?: {transaction.is_valid()}")


