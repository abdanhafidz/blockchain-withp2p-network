from View import TransactionView
def Control():
    try:
        SendTo, RecvID, Message =  TransactionView.Main()
        if(SendTo and RecvID and Message):
            None
    except Exception as err:
        return err