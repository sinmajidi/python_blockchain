import hashlib
import datetime
dificulty_check="000000000000000000000000000000";
class Block:
	def __init__(self,index,data,previousHash=''):
		self.index=index
		self.timestamp=str(datetime.datetime.now())
		self.data=data
		self.previousHash=previousHash
		self.nonce=0
		self.hash=self.calculateHash()

	def calculateHash(self):
		return hashlib.sha256(str(self.index).encode('utf-8')
		                      + self.previousHash.encode('utf-8')
		                      + str(self.data).encode('utf-8')
		                      + self.timestamp.encode('utf-8')+str(self.nonce).encode('utf-8')).hexdigest()
	def showblock(self):
		print("index: "+str(self.index)+"---"+"data: "+str(self.data)+"---"+"time: "+str(self.timestamp)+"---"+"hash: "+str(self.hash)+"---"+"pre_hash: "+str(self.previousHash))

	def mineBlock(self,difficulty):

		while (self.hash[:difficulty]!= dificulty_check[:difficulty]):
			self.nonce+=1
			self.hash = self.calculateHash();
