from Blockchain import Blockchain

newCoin = Blockchain()
minerRewardAddress = "MinerRewardAddress"

# Transactions
newCoin.createTransaction("WalletAddress1", "WalletAddress2", 5)
newCoin.createTransaction("WalletAddress2", "WalletAddress1", 2)

print("Mining pending transactions...")
newCoin.minePendingTransactions(minerRewardAddress)

# Check wallet balances
print("WalletAddress1 Balance:", newCoin.getWalletBalance("WalletAddress1"))
print("WalletAddress2 Balance:", newCoin.getWalletBalance("WalletAddress2"))
print("MinerRewardAddress Balance after mining:", newCoin.getWalletBalance("MinerRewardAddress"))

