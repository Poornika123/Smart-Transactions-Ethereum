
import time
from hashlib import *
import streamlit as st

blockNames = [] 
BlockIds =  []

zeros = 5

class transaction:
    def __init__(self,fromadd,toadd,amount):
        self.fromadd=fromadd
        self.toadd=toadd
        self.amount=amount
        self.time = time.time()

        self.transobj = {'Sender_Address':self.fromadd,'Recipient_Address':self.toadd,'Amount':self.amount,'Time':self.time}
        Blockchain.pendingtrans.append(self.transobj)

class Block:
    blockindex = 1
    def __init__(self,ts,data,prevhash='0'):
        self.index=Block.blockindex
        Block.blockindex+=1
        self.ts = ts
        self.data=data
        self.nonce=0
        self.prevhash=prevhash
        self.hash=self.pow()

    def calcHash(self):
        return sha256((str(str(self.data)+str(self.nonce)+str(self.ts)+self.prevhash)).encode('utf-8')).hexdigest()

    def blockData(self):
        text1 = ("Block number: "+ str(self.index))
        text2 = ("Block timestamp: "+ str(self.ts))
        text3 = ("Block data: "+ str(self.data))
        text4 = ("Nonce: "+ str(self.nonce))
        text5 = ("Block previous hash: "+ str(self.prevhash))
        text6 = ("Block hash: "+ str(self.hash))

        FinalText = text1 + "\n" + text2 + "\n" +text3 + "\n" + text4 + "\n" + text5 + "\n"  + text6 + "\n"

        return FinalText


    def pow(self,zero=zeros):
        self.nonce=0
        while(self.calcHash()[:zero]!='0'*zero):
            self.nonce+=1
        return self.calcHash()


class Blockchain:
    pendingtrans=[]
    def __init__(self):
        self.chain = []

    def genesis(self):
        return Block(time.time(),'data in genesis')

    def addGenesis(self): #addBlock vale method me if length of chain is 0 --> add genesis block se ho sakta tha but...
        self.chain.append(self.genesis()) #baar baar block add karne pe ek if condition bar bar execute hoti faltu me

    def load_trans_in_block(self,index):
        pass


    def addBlock(self,newBlock):

        newBlock.prevhash=self.chain[len(self.chain)-1].hash
        newBlock.hash=newBlock.pow()
        self.chain.append(newBlock)
        print(newBlock.blockData())

    def valid(self):
        for i in range(1,len(self.chain)):
            if self.chain[i].hash!=self.chain[i].calcHash():
                return False
            if self.chain[i-1].hash!=self.chain[i].prevhash:
                return False

        return True

    def displayChain(self):

        List = []

        for i in range(len(self.chain)):
            st.write(self.chain[i].blockData())
            List.append(self.chain[i].blockData())

        return List
