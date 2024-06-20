import datetime
class Block:
    def __init__(self, hash = "", prev_hash = "", message = "", nonce = "", proof_of_work = "", number_of_block = 0, timeStamp = "", signature = ""):
        self.hash = hash
        self.prev_hash = prev_hash
        self.message = message
        self.nonce = nonce
        self.proof_of_work = proof_of_work
        self.number_of_block = number_of_block
        self.signature = signature
        self.timeStamp = str(datetime.datetime.now())
class BlockVerifyStatus:
    def __init__(self):
        self.BlockNumber = 0
        self.Status = True
        self.PreviousHashBlockError = False
        self.InvalidBlockHash = False
        self.InvalidSignature = False
        self.BlocksFork = False
        self.MissedBlock = False
class Response:
    def __init__(self, Data, Message):
        self.Data = Data
        self.Error = False
        self.Message = Message
class DictObj:
    def __init__(self, dict1):
        self.__dict__.update(dict1)
    
    def __getitem__(self, key):
        return self.__dict__[key]
    
    def __setitem__(self, key, value):
        self.__dict__[key] = value
    
    def __delitem__(self, key):
        del self.__dict__[key]
    
    def __repr__(self):
        return f"{self.__dict__}"
