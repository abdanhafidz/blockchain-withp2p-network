
from Controller import NodeController, TransactionController
from View import MenuView
import os
def LoadView(loc):
    # os.system('cls')
    try:
        match loc:
            case 0:
                NodeController.Control()
            case 1:
                TransactionController.Control()
            case 2:
                NodeController.Control()
            case 3:
                NodeController.Control()
            case _:
                print("Error : Invalid Menu Command")
                NodeController.Control()
        MenuView.Main()
    except KeyboardInterrupt:
        s = input("Exit the Program? [Y/n] :")
        if(s == "Y"):
            print("Goodbye! ^^")
            exit()
        else:
            os.system('cls')
            NodeController.Control()
    except TypeError:
        print('An Error Occured : ','Invalid Command #', loc)
    except Exception as error:
        os.system('cls')
        print('An Error Occured : ','Invalid Command #', error)
        NodeController.Control()