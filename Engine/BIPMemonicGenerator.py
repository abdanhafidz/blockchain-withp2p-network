from mnemonic import Mnemonic
import hashlib

def CreateMemonicPhrase(private_key):
    private_key_hex = private_key
    private_key_bytes = bytes.fromhex(private_key_hex)
    entropy = hashlib.sha256(private_key_bytes).digest()
    mnemonic = Mnemonic("english").to_mnemonic(entropy[:32])
    return mnemonic