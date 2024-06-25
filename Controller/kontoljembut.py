import pandas as pd
from Database import Repositories as DB
from tabulate import tabulate
def print_table(data):
    print(data)
    

def Control():
    try:
        data = DB.GetBlockChainData()
        print_table(data)
    except Exception as e:
        print(e)