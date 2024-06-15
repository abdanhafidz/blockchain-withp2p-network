import datetime
import json
from Models import Block
import random
from Engine import Hash, JSONWorker

class Blockchain:
    def __init__(self):
        BlockChainData = JSONWorker.GetDataJSON('Database/BlockChainDB.json')
        self.blockchaindata = list(BlockChainData)
        
    def add_block(self, block:Block):
        dictBlock = {
            "hash": block.hash, 
            "prev_hash": block.prev_hash, 
            "message": block.message,
            "nonce": block.nonce, 
            "proof_of_work": block.proof_of_work, 
            "number_of_block": len(self.blockchaindata) + 1, 
            "timeStamp": block.timeStamp
        }
        self.blockchaindata.append(dictBlock)
        return JSONWorker.CreateDataJSON('Database/BlockChainDB.json',self.blockchaindata)
        
    def mine_block(self, block:Block):
        previous_block = self.blockchaindata[-1]
        print(previous_block)
        # print(previous_block)
        data = JSONWorker.GetDataJSON('Database/NodeDB.json')
        previous_hash = previous_block["hash"]
        publicKey = data['PublicKey']
        works = 0
        print(previous_block["nonce"])
        for mineNonce in range(1,2**(256)):
            hash_hex = str(hash(block.message, previous_hash, publicKey, mineNonce))
            hash_binary = ''.join(format(ord(x), '08b') for x in hash_hex)  
            
            if(str(hash_binary)[:2] == "00"):
                block.prev_hash = previous_hash
                block.nonce = mineNonce
                block.hash = hash_hex
                block.proof_of_work = works
                break
            else:
                # print(hash_hex)
                # print(hash_binary)
                # print(str(hash_binary)[:2])
                print("Mining block on step : ", works)
                works+=1
        self.add_block(block)
        return block
    def verify_block(self):
        for i in range(1, len(self.blockchaindata)):
            previous_block = self.blockchaindata[i - 1]
            current_block = self.blockchaindata[i]
            if current_block["previous_hash"] != self.hash(previous_block):
                return False
        return True
    

# blockBaru = Block()
# blockBaru.message = "Naufal Transfer 20 BTC"
# BlockChain = Blockchain()
# BlockChain.mine_block(blockBaru)