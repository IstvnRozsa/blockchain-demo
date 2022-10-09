from block import Block
from transaction import Transaction
from datetime import datetime

from wallet import Wallet

class BlockChain:
    def __init__(self):
        # Genesis block
        self.__chain = [Block(datetime.now(),"Genesis")]
        self.__difficulty = 4
        if self.__chain[0].get_prev_hash() is None:
            self.__chain[0].mine_block(self.__difficulty)


    def get_last_block(self):
        return self.__chain[-1]


    def add_block(self, new_block):
        new_block.set_prev_hash(self.get_last_block().get_hash())
        new_block.mine_block(self.__difficulty)
        self.__chain.append(new_block)

    def show_chain(self):
        print("-"*10 + "Start" +"-"*10)
        for block in self.__chain:
            print("-"*10)
            print(block)
            block.show_transactions()

    def is_chain_valid(self):
        for index, block in enumerate(self.__chain):
            current_block = self.__chain[index]
            previous_block = self.__chain[index - 1]

            if current_block.get_hash().hexdigest() != current_block.calculate_hash().hexdigest():
                return False
            if current_block.get_prev_hash() is not None:
                if current_block.get_prev_hash().hexdigest() != previous_block.get_hash().hexdigest():
                    # itt fut bele print("Corrupt Block:\n", previous_block)
                    return False
        return True

    # Only for test
    def change_chain(self, i:int, to_wallet:Wallet, amount:int):
        self.__chain[i].change_block_data(to_wallet, amount)



if __name__ == "__main__":
    pityuCoin = BlockChain()
    
    bob_wallet = Wallet("Bob")
    jack_wallet = Wallet("Jack")
    transaction1 = Transaction(bob_wallet, jack_wallet, 10)
    transaction2 = Transaction(jack_wallet, bob_wallet, 10)
    pityuCoin.add_block(Block(datetime.now(), transaction1.transaction_hash, [transaction1]))
    pityuCoin.add_block(Block(datetime.now(), transaction2.transaction_hash, [transaction2]))
    pityuCoin.show_chain()
    print(f"Is Chain Valid? {pityuCoin.is_chain_valid()}")


    hacker_wallet = Wallet("Hacker")
    pityuCoin.change_chain(1, hacker_wallet, 250)
    pityuCoin.show_chain()
    print(f"Is Chain Valid? {pityuCoin.is_chain_valid()}")


