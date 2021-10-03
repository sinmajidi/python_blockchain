from Blockchainclass import BlockChain
from Blockclass import Block

pycoin = BlockChain();
pycoin.addBlock(Block(1, 'amount: 4'));
pycoin.addBlock(Block(2, 'amount: 33'));
pycoin.chain[1].data = 'amount : 1000'
pycoin.chain[1].hash = pycoin.chain[1].calculateHash()
for i in pycoin.chain:
	i.showblock()
print("Is the blockchain valid? " + str(pycoin.isChainValid()) );
