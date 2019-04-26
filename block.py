import hashlib
import datetime

#creation du data du block

class block:
	#initialisation du block avec le precedent celui en cours et le temp(de ce que j'ai compris)
	#probleme sur cet ligne j'ai probablement fait une erreur de syntaxe
	def __init__(self,previous_block_hash, data, timestamp):
		self.previous_block_hash = previous_block_hash
		self.data = data
		self.timestamp = timestamp
		self.hash = self.get_hash()


#creation du block d'origine

	@staticmethod
	def creation_origin_block():
		return block("0","0",datetime.datetime.now())


#fonction de hashage

	def get_hash(self):
		header_bin= (str(self.previous_block_hash) +str(self.data) + str(self.timestamp)).encode()


					#sha256 est un algorithme de hachage
		inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
		outer_hash = hashlib.sha256(inner_hash).hexdigest()
		return outer_hash
