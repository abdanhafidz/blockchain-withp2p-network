import hashlib
import json

def hash(currentBlock, prevHash, signature, nonce, timeStamp):
    payLoad = str(currentBlock + prevHash + signature + str(nonce) + str(timeStamp))
    return hashlib.sha256((payLoad).encode('utf-8')).hexdigest()
