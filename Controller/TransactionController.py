from View import TransactionView
from Models import Block, Blockchain
from Database import Repositories
from Engine import JSONWorker
def Control():
    try:
        SendTo, RecvID, Message =  TransactionView.Main()
        BlockChain = Blockchain.Blockchain()
        NewBlock = Block.Block()
        PublicKey = Repositories.GetUserData('PublicKey')
        NewBlock.message = f"From {PublicKey} to {RecvID}, {Message}"
        MinedBlock = BlockChain.mine_block(NewBlock)
        JSONWorker.CreateDataJSON('Buffer/WaitBox.json',{"Draft":MinedBlock.__dict__})
        print("Transaction Created With Block : ", MinedBlock.__dict__)
    except Exception as err:
        print(err)
        return err