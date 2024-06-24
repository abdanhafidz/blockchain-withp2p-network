from Loader import Loader

def Main():
    print('''
    --- Menu ---
    1. Create Transaction
    2. Get Transacation History
    3. Get Local Block-Chain Data
    0. Return to main Menu
          ''')
    cm = int(input("Choose Menu [1/2/3/0] :"))
    Loader.LoadView(cm)