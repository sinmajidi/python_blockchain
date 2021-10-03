from Blockclass import Block
class BlockChain:
	def __init__(self):
		self.chain = [self.createGenesisBlock()]

	def createGenesisBlock(self):
	  return Block(0, "Genesis Block", "0");

	def getLastestBlock(self):
		return self.chain[len(self.chain) - 1];

	def addBlock(self,newBlock):

		newBlock.previousHash = self.getLastestBlock().hash;
		newBlock.hash = newBlock.calculateHash();
		self.chain.append(newBlock);
		