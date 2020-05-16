import random as rd
def numberGuess():
    num = rd.randint(1,100)
    inp = -1
    while(num != inp and inp != 0):
        inp = int(input("Enter Guess Between 1 and 100 (Guess 0 to exit): "))
        if(inp != 0):
            if(inp > num):
                print("Number is smaller than the entered number")
            elif(inp < num):
                print("Number is larger than the entered number")
    if(inp != 0):
        print("Congrats! Correct Guess!")
    else:
        print("Game Over")

numberGuess()