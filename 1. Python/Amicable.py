import math
# Function to find sum of proper divisors of a number
def divisorSum(n):
    result = 0
    i = 2
    while i <= (math.sqrt(n)):
        if (n % i == 0):
            if (i == (n / i)):
                result = result + i
            else:
                result = result + (i + n / i)
        i = i + 1
    return (result + 1)
# Function to print first n amicable number pairs

def printAmicable(n):
    count = 0
    num = 2.0
    last = 0
    while count != n:
        num2 = divisorSum(num)
        sum = divisorSum(num2)
        if(sum == num and num2 != num and num != last):
            print(num, ",", num2)
            count+=1
            last = num2
        num+=1

printAmicable(10)