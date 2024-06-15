from View import TransactionView
from Network import Handler
from Models import Block, Blockchain
from Database import Repositories
from Engine import JSONWorker
def Control():
    try:
        SendTo, RecvID, Message =  TransactionView.Main()
        if(SendTo and RecvID and Message):
            BlockChain = Blockchain.Blockchain()
            NewBlock = Block.Block()
            PublicKey = Repositories.GetUserData["PublicKey"]
            NewBlock.message = "From {PublicKey} to {SendTo}, {Message}"
            MinedBlock = BlockChain.mine_block(NewBlock)
            JSONWorker.CreateDataJSON('Buffer/WaitBox.json',{"Draft":MinedBlock.__dict__})
            print("Transaction Created With Block : ", MinedBlock.__dict__)
    except Exception as err:
        return err