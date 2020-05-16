import random as rd
def dice():
    while(1):
        choice = input("Roll Dice(Y/N)? ")
        if(choice == "N"):
            exit()
        elif(choice != "Y"):
            print("Invalid Choice")
            exit()
        else:
            num = rd.randint(1,6)
            print("Number Obtained:", num)

dice()
