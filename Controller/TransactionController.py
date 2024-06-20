from View import TransactionView
from Models import Blockchain, Interface
from Database import Repositories
from Middleware import JSONWorker, BlockChainSync
def Control():
    try:
        BlockChainSync.VerifySyncBlockChain()
        SendTo, RecvID, Message =  TransactionView.Main()
        BlockChain = Blockchain.Blockchain()
        NewBlock = Interface.Block()
        PublicKey = Repositories.GetUserData('PublicKey')
        NewBlock.message = f"From {PublicKey} to {RecvID}, {Message}"
        MinedBlock = BlockChain.mine_block(NewBlock)
        JSONWorker.CreateDataJSON('Buffer/WaitBox.json',{"Draft":MinedBlock.__dict__})
        print("Transaction Created With Block : ", MinedBlock.__dict__)
    except Exception as err:
        print(err)
        return err