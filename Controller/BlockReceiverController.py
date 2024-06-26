from Models.Interface import Block, BlockVerifyStatus, Response, DictObj
from Models.Blockchain import Blockchain
from Middleware.KeyGenerator import ParseSender
from Database import Repositories as DB
from Middleware import JSONWorker, BlockChainSync
def Control(block:DictObj)->Response:
    try:
        block = DictObj(block)
        BlockChainSync.VerifySyncBlockChain()
        BlockChain = Blockchain()
        VerifyBlock:BlockVerifyStatus = BlockChain.verify_block(block)
        if VerifyBlock.Status:
                BlockChain.add_block(block)
        elif VerifyBlock.BlocksFork:
            LastBlock =  BlockChain.BlockChainData[-1]
            LastBlockProof  = LastBlock["proof_of_work"]
            LastBlockCreator = ParseSender(LastBlock["message"])
            BlockProof = block.proof_of_work
            BlockCreator = ParseSender(block["message"])
            if(LastBlockProof > BlockProof):
                if(BlockCreator == DB.GetUserData("PublicKey")):
                    MinedBlock = BlockChain.mine_block(block)
                    JSONWorker.CreateDataJSON('Buffer/WaitBox.json',{"Draft":MinedBlock.__dict__})
                elif(BlockProof > LastBlockProof):
                    BlockChain.remove_block()
                    BlockChain.add_block(block)
                    if(LastBlockCreator == DB.GetUserData("PublicKey")):
                        MinedBlock = BlockChain.mine_block(LastBlock)
                        JSONWorker.CreateDataJSON('Buffer/WaitBox.json',{"Draft":MinedBlock.__dict__})
        elif VerifyBlock.MissedBlock:
            print("Invalid Block Received, Need to Synchronize")
            BlockChainSync.SynchronizeBlockChain()
        else:
            print('Block Verify Failed : ',VerifyBlock.__dict__, 'Block Denied')
    except Exception as err:
        print(err)
        return err