import hashlib
import json

def hash(currentBlock, prevHash, privateKey, nonce):
    return hashlib.sha256(("currentBlock"+"prevHash"+"privateKey"+"nonce").encode('utf-8')).hexdigest()