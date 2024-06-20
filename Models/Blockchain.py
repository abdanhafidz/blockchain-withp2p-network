import datetime
from Models.Interface import Block, BlockVerifyStatus, DictObj
from Database import Repositories as DB
from Middleware import Hash, KeyGenerator 
from typing import Union
class Blockchain:
    def __init__(self):
        BlockChainData = DB.GetBlockChainData()
        self.BlockChainData = list(BlockChainData)
    def add_block(self, block:Union[DictObj,'Block',Block]):
        block.timeStamp = str(datetime.datetime.now())
        dictBlock = block.__dict__
        self.BlockChainData.append(dictBlock)
        DB.CreateBlockChainData(self.BlockChainData)
    def remove_block(self):
        self.BlockChainData.pop()
        DB.CreateBlockChainData(self.BlockChainData)
    def mine_block(self, block:Union[DictObj,'Block',Block]):
        previous_block = self.BlockChainData[-1]
        block.number_of_block = len(self.BlockChainData) + 1
        data = DB.GetUserData
        previous_hash = previous_block["hash"]
        privateKey = data('PrivateKey')
        signature = str(KeyGenerator.sign_message(privateKey,str(block.message + block.timeStamp)).hex())
        block.signature = signature
        works = 0
        for mineNonce in range(1,2**(256)):
            hash_hex = str(Hash.hash(block.message, previous_hash, signature, mineNonce, block.timeStamp))
            hash_binary = ''.join(format(ord(x), '08b') for x in hash_hex)  
            if(str(hash_binary)[:2] == "00"):
                block.prev_hash = previous_hash
                block.nonce = mineNonce
                block.hash = hash_hex
                block.proof_of_work = works
                break
            else:
                print("Mining block on Works :", works)
                works+=1
        self.add_block(block)
        return block
    def verify_block(self, block:Union[DictObj,'Block',Block])->BlockVerifyStatus:
        HashHex = str(Hash.hash(block.message, self.BlockChainData[-1]["hash"], block.signature, block.nonce, block.timeStamp))
        PublicKey = KeyGenerator.load_public_key_from_hex(KeyGenerator.ParseSender(block.message))
        VerifySignature = KeyGenerator.verify_signature(PublicKey, block.message, block.signature)
        VerifyStatus = BlockVerifyStatus()
        if(self.BlockChainData[-1]["hash"] == block.prev_hash and block.hash == HashHex and VerifySignature and block.number_of_block == self.BlockChainData[-1]["number_of_block"] + 1):
            return True
        else:
            if(self.BlockChainData[-1]["hash"] != block.prev_hash):
                VerifyStatus.PreviousHashBlockError = True
                if(self.BlockChainData[-1]["prev_hash"] == block.prev_hash):
                    VerifyStatus.BlocksFork = True
            if(block.hash != HashHex):
                VerifyStatus.InvalidBlockHash = True
            if(not VerifySignature):
                VerifyStatus.InvalidSignature = True
            if(block.number_of_block != self.BlockChainData[-1]["number_of_block"] + 1):
                VerifyStatus.MissedBlock = True
            VerifyStatus.BlockNumber = block.number_of_block
            return VerifyStatus
    def verify_chain(self):
        for data in self.BlockChainData[::-1]:
            if(data["number_of_block"] == 0): continue
            if(not self.verify_block(DictObj(data)).Status):
                return False
        return True

# blockBaru = Block()
# blockBaru.message = "Naufal Transfer 20 BTC"
# BlockChain = Blockchain()
# BlockChain.mine_block(blockBaru)