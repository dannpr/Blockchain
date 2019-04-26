from block import block
import datetime

#on cree notre liste de block avec le premier lock du nom de origins block

block_chain = [block.creation_origin_block()]

print("le block d'origine a ete cree!!")
#son code hash qui nous lie a notre block (en cas de modification le hash changera) 
print("Hash:%s " % block_chain[-1].hash)

#creaton de 5 blocks , chaque nouveau est ajoute au dernier

num_of_blocks_to_add = 5

#i : int 
for i in range(1, num_of_blocks_to_add+1):
	#rajout dans la "liste" de block soit une blockchain

	block_chain.append(block(block_chain[-1].hash,"veullez entrer une transaction ",datetime.datetime.now()))

	print("Block #%d a ete cree" % i)
	print("Block #%d hash: %s" % (i, block_chain[i].hash))


