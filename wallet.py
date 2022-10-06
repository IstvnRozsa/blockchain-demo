import rsa


class Wallet:
    def __init__(self, name):
        self.name = name
        self.public_key, self.private_key = rsa.newkeys(1024)
    

if __name__ == "__main__":
    wallet = Wallet("Bob")
    print(wallet.name)
    print(wallet.private_key)
    print(wallet.public_key)