import json
from Models.Interface import DictObj
def GetDataJSON(JSONFile):
    with open(JSONFile, 'r') as f:
        data = json.load(f)
        json.loads(json.dumps(data), object_hook=DictObj)
    return data
def CreateDataJSON(JSONFile, Data):
    with open(JSONFile, "w") as outfile:
        json.dump(Data, outfile)
    return Data
def EditDataJSON(JSONFile,param,val):
    data = GetDataJSON(JSONFile)
    data[param] = val
    return CreateDataJSON(JSONFile,data)
    