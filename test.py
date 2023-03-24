from ethereum import Blockchain, Block
import time

chain = Blockchain()
chain.addGenesis()
b2 = Block(time.time(),'some data in 2nd block')
b3 = Block(time.time(),'data in 3rd block')
chain.addBlock(b2)
chain.addBlock(b3)

print("Chain is here")

print(chain.displayChain())