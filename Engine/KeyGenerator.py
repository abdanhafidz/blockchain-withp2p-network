from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError
def load_private_key_from_hex(hex_string):
    private_key_bytes = bytes.fromhex(hex_string)
    private_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    return private_key
def generate_key_pair():
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key
def sign_message(private_key_hex, message):
    private_key = load_private_key_from_hex(private_key_hex)
    return private_key.sign(message.encode('utf-8'))

def verify_signature(public_key, message, signature):
    try:
        return public_key.verify(signature, message)
    except BadSignatureError:
        return False