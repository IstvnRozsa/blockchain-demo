from block import Block
from transaction import Transaction
from datetime import datetime

class BlockChain:
    def __init__(self):
        # Genesis block
        self.__chain = [Block(datetime.now(),Transaction("Alice", "Bob", 100))]
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
        for block in self.__chain:
            print(block)

    def is_chain_valid(self):
        for index, block in enumerate(self.__chain):
            current_block = self.__chain[index]
            previous_block = self.__chain[index - 1]

            if current_block.get_hash().hexdigest() != current_block.calculate_hash().hexdigest():
                return False
            if current_block.get_prev_hash() is not None:
                if current_block.get_prev_hash().hexdigest() != previous_block.get_hash().hexdigest():
                    return False
        return True

    # Only for test
    def change_chain(self):
        self.__chain[0].change_block_data()



if __name__ == "__main__":
    pityuCoin = BlockChain()
    
    pityuCoin.add_block(Block(datetime.now(), Transaction("Takamoto", "Jomashita", 100)))
    pityuCoin.add_block(Block(datetime.now(), Transaction("Yakashima", "Takamoto", 50)))
    pityuCoin.show_chain()
    print(f"Is Chain Valid? {pityuCoin.is_chain_valid()}")

    pityuCoin.change_chain()

    pityuCoin.add_block(Block(datetime.now(), Transaction("Takamoto", "Jomashita", 80)))
    pityuCoin.add_block(Block(datetime.now(), Transaction("Yakashima", "Takamoto", 50)))
    pityuCoin.show_chain()
    print(f"Is Chain Valid? {pityuCoin.is_chain_valid()}")


