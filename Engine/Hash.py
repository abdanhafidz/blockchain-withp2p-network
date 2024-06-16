import hashlib
import json

def hash(currentBlock, prevHash, signature, nonce):
    payLoad = str(currentBlock + prevHash + signature + str(nonce))
    return hashlib.sha256((payLoad).encode('utf-8')).hexdigest()