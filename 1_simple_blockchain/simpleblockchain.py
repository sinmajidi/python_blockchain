from Blockchainclass import BlockChain
from Blockclass import Block

pycoin = BlockChain()
pycoin.addBlock(Block(1, 'amount: 4'))
pycoin.addBlock(Block(2, 'amount: 33'))
for i in pycoin.chain:
	i.showblock()

