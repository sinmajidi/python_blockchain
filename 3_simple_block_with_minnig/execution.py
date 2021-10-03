from Blockchainclass import BlockChain
from Blockclass import Block

pycoin = BlockChain();
print("minig block1")
pycoin.addBlock(Block(1, 'amount: 4'));
print("minig block2")
pycoin.addBlock(Block(2, 'amount: 33'));
print("minig block3")
pycoin.addBlock(Block(3, 'amount: 5.5'));
#pycoin.chain[1].data = 'amount : 1000'
#pycoin.chain[1].hash = pycoin.chain[1].calculateHash()
for i in pycoin.chain:
	i.showblock()
print("Is the blockchain valid? " + str(pycoin.isChainValid()) );
