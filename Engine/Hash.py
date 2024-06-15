import hashlib
import json

def hash(currentBlock, prevHash, publicKey, nonce):
    payLoad = str(currentBlock + prevHash + publicKey + str(nonce))
    return hashlib.sha256((payLoad).encode('utf-8')).hexdigest()