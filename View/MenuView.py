from Loader import Loader

def Main():
    print('''
    --- Menu ---
    1. Create Transaction
    2. Get Transacation History
    3. Get Local Block-Chain Data
    4. Get Another Node Block-Chain Data (Random)
    5. Verify A Transaction
    0. Return to main Menu
          ''')
    cm = int(input("Choose Menu [1/2/3/4/5/0] :"))
    Loader.LoadView(cm)