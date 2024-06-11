from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError
def generate_key_pair():
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key
def sign_message(private_key, message):
    return private_key.sign(message)

def verify_signature(public_key, message, signature):
    try:
        return public_key.verify(signature, message)
    except BadSignatureError:
        return False
privKey, pubKey = generate_key_pair()


