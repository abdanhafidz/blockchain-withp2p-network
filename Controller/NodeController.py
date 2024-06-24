from Database import Repositories as repo
from Middleware import KeyGenerator as KeyGen, BIPMemonicGenerator as MemonicGen
from View import HomeView
import json, socket
def Control():
    # try:
    PrivateKey = repo.GetUserData("PrivateKey")
    PublicKey = repo.GetUserData("PublicKey")
    hostname = socket.gethostname()
    NodeAddress = socket.gethostbyname(hostname)
    if(PrivateKey == None  or PublicKey == None or  PrivateKey == "" or PublicKey == ""):
        print("Generating Credential Keys ... ")
        private_key, public_key = KeyGen.generate_key_pair()
        PrivateKey = private_key.to_string().hex()
        PublicKey = public_key.to_string("compressed").hex()
        JsonObject = json.dumps({
            "NodeAddress":NodeAddress,
            "PrivateKey":PrivateKey,
            "PublicKey":PublicKey
        }, indent = 3)
        with open("Database/NodeDB.json", "w") as outfile:
            outfile.write(JsonObject)
        Memonic = MemonicGen.CreateMemonicPhrase(private_key)
        HomeView.Main(Memonic, PublicKey)
    else:
        JsonObject = json.dumps({
            "NodeAddress":NodeAddress,
            "PrivateKey":PrivateKey,
            "PublicKey":PublicKey
        }, indent = 3)
        with open("Database/NodeDB.json", "w") as outfile:
            outfile.write(JsonObject)
        Memonic = MemonicGen.CreateMemonicPhrase(PrivateKey)
        HomeView.Main(Memonic, PublicKey)
    # except Exception as err:
    #     print("X) An Error Occurred : ", err)
    #     exit()