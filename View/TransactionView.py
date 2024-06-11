def Main():
    print('''
    * Transaction Menu *
          ''')
    SendTo = input("Receiver Address:")
    RecvID = input("Receiver ID:")
    Message = input("Message:")
    conf = input("Confirm The Transaction [Y/n] :")
    if(conf == "Y"):
        return SendTo, RecvID, Message
    else:
        print("Transaction Canceled")
        return False
    