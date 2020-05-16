#Function to print all Armstrong Numbers in a given range
def ArmstrongRange(start, end):
    for i in range(start, end + 1):
        check = 0
        l = [int(j) for j in str(i)]
        for j in l:
            check += j**3
        if(check == i):
            print(i)

s = int(input("Enter Start of Range:"))
e = int(input("Enter End of Range:"))
ArmstrongRange(s, e)
