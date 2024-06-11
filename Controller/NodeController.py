from Database import Repositories as repo
from Engine import KeyGenerator as KeyGen, BIPMemonicGenerator as MemonicGen
from View import HomeView
import json, random
def Control():
    try:
        NodeAddress = int(repo.GetUserData("NodeAddress"))
        PrivateKey = repo.GetUserData("PrivateKey")
        PublicKey = repo.GetUserData("PublicKey")
        if(NodeAddress <= 0):
            NodeAddress = random.randint(100000000000,10000000000000)
            print("Looks Like you Are a new User ... wait for us creating Ur Credentials")
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
            Memonic = MemonicGen.CreateMemonicPhrase(PrivateKey)
            HomeView.Main(Memonic, PublicKey)
    except Exception as err:
        print("X) An Error Occurred : ", err)
        exit()