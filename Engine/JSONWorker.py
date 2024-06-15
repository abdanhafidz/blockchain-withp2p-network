import json
def GetDataJSON(JSONFile):
    f = open(JSONFile)
    data = json.load(f)
    return data
def CreateDataJSON(JSONFile, Data):
    with open(JSONFile, "w") as outfile:
        json.dump(Data, outfile)
    return Data
    