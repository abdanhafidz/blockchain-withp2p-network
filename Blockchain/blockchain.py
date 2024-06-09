import datetime
import json
from block import Block
from hash_function import hash

class Blockchain:
    def __init__(self):
        f = open("../Database/block_chain_db.json")
        BlockChainData = json.load(f)
        print(BlockChainData)
        self.blockchaindata = list(BlockChainData)
        
    def add_block(self, block:Block):
        dictBlock = {
            "hash": block.hash, 
            "prev_hash": block.prev_hash, 
            "message": block.message,
            "nonce": block.nonce, 
            "proof_of_work": block.proof_of_work, 
            "number_of_block": 1, 
            "timeStamp": block.timeStamp
        }
        self.blockchaindata.append(dictBlock)
        with open("../Database/block_chain_db.json", "w") as outfile:
            json.dump(self.blockchaindata, outfile)
        
    def mine_block(self, block:Block):
        previous_block = self.blockchaindata[-1]
        print(previous_block)
        f = open("../Database/user_db.json")
        data = json.load(f)
        previous_hash = previous_block["hash"]
        private_key = data['PrivateKey']
        block.hash = hash(block.message, previous_hash, private_key, 123782)
        self.add_block(block)
    
    def verify_block(self):
        for i in range(1, len(self.blockchaindata)):
            previous_block = self.blockchaindata[i - 1]
            current_block = self.blockchaindata[i]
            if current_block["previous_hash"] != self.hash(previous_block):
                return False
        return True
    

blockBaru = Block()
blockBaru.message = "Naufal Transfer 20 BTC"
blockBaru.timeStamp = str(datetime.datetime.now())
BlockChain = Blockchain()
BlockChain.mine_block(blockBaru)