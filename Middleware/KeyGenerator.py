from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError
def ParseSender(msg : str):
    return (msg.split("From ")[1]).split()[0]
def load_private_key_from_hex(hex_string):
    private_key_bytes = bytes.fromhex(hex_string)
    private_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    return private_key
def load_public_key_from_hex(hex_string: str):
    public_key_bytes = bytes.fromhex(hex_string)
    public_key = VerifyingKey.from_string(public_key_bytes, curve=SECP256k1)
    return public_key
def generate_key_pair():
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key
def sign_message(private_key_hex, message):
    private_key = load_private_key_from_hex(private_key_hex)
    return private_key.sign(message.encode('utf-8'))

def verify_signature(public_key, message, signature):
    try:
        return public_key.verify(bytes.fromhex(signature), message.encode('utf-8'))
    except BadSignatureError:
        return False