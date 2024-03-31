from Block import Block, Transaction

class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 6
        self.pendingTransactions = []

    def createGenesisBlock(self):
        return Block(0, [])

    def getLastestBlock(self):
        return self.chain[-1]

    def minePendingTransactions(self, minerRewardAddress):
        block = Block(len(self.chain), self.pendingTransactions)
        block.mineBlock(self.difficulty)
        print("Block successfully mined.")
        self.chain.append(block)
        self.pendingTransactions = [Transaction(None, minerRewardAddress, 0.1)]  # Reward for mining

    def createTransaction(self, sender, recipient, amount):
        self.pendingTransactions.append(Transaction(sender, recipient, amount))

    def getWalletBalance(self, walletAddress):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.recipient == walletAddress:
                    balance += transaction.amount
                if transaction.sender == walletAddress:
                    balance -= transaction.amount
        # Check for mining rewards
        for transaction in self.pendingTransactions:
            if transaction.recipient == walletAddress:
                balance += transaction.amount
        return balance


    def isChainValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i - 1]
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            if currentBlock.previousHash != previousBlock.hash:
                return False
        return True
