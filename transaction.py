import rsa
import hashlib



class Transaction:
    def __init__(self, sender, receiver, amount):
        self.__sender = sender 
        self.__receiver = receiver
        self.__amount = amount
        self.signature = None
        self.transaction_hash = self.calculate_hash()

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

    def sign_transaction(self, wallet):
        self.signature = rsa.sign(self.transaction_hash.encode(), wallet.private_key, "SHA-256")

    def is_valid(self):
        try:
            rsa.verify(self.transaction_hash.encode(), self.signature, self.__sender.public_key)
            return True
        except rsa.VerificationError:
            return False
    
    # Only test
    def hack_transaction(self, wallet):
        self.__amount = 1000000
        self.__receiver = wallet
        self.transaction_hash = self.calculate_hash()



if __name__=="__main__":
    from wallet import Wallet

    bob_wallet = Wallet("Bob")
    jack_wallet = Wallet("Jack")

    transaction = Transaction(bob_wallet, jack_wallet, 10)
    
    transaction.sign_transaction(bob_wallet)
    print(transaction)
    print(f"Transaction valid?: {transaction.is_valid()}")

    print("-"*30)
    hacker_wallet = Wallet("Hacker")
    transaction.hack_transaction(hacker_wallet)
    print(transaction)
    print(f"Transaction valid?: {transaction.is_valid()}")


