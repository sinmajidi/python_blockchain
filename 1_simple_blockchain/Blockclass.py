import hashlib
import datetime

class Block:
	def __init__(self,index,data,previousHash=''):
		self.index=index
		self.timestamp=str(datetime.datetime.now())
		self.data=data
		self.previousHash=previousHash
		self.hash=self.calculateHash()

	def calculateHash(self):
		return hashlib.sha256(str(self.index).encode('utf-8')
		                      + self.previousHash.encode('utf-8')
		                      + str(self.data).encode('utf-8')
		                      + self.timestamp.encode('utf-8')).hexdigest()
	def showblock(self):
		print("index: "+str(self.index)+"---"+"data: "+str(self.data)+"---"+"time: "+str(self.timestamp)+"---"+"hash: "+str(self.hash)+"---"+"pre_hash: "+str(self.previousHash))
