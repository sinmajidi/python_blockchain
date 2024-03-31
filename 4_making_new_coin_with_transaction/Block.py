import hashlib
import datetime

difficulty_check = "00000000000000000"

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __str__(self):
        return f"{self.sender} sends {self.amount} sinaCoins to {self.recipient}"

class Block:
    def __init__(self, index, transactions, previousHash=''):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.transactions = transactions
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        return hashlib.sha256((str(self.index) + self.previousHash + str(self.transactions) + self.timestamp + str(self.nonce)).encode()).hexdigest()

    def showBlock(self):
        print("Index: " + str(self.index) +
              " | Transactions: " + str([str(transaction) for transaction in self.transactions]) +
              " | Timestamp: " + str(self.timestamp) +
              " | Hash: " + str(self.hash) +
              " | Previous Hash: " + str(self.previousHash))

    def mineBlock(self, difficulty):
        while self.hash[:difficulty] != difficulty_check[:difficulty]:
            self.nonce += 1
            self.hash = self.calculateHash()
