#Function to print first n numbers of a geometric sequence
def printGeometric(a, r, n):
        for i in range(0, n):
            print(a * (r**i))

a = float(input("Enter Initial Value:"))
r = float(input("Enter Common Ratio:"))
print("First 10 Numbers in the Geometric Series are:")
printGeometric(a, r, 10)