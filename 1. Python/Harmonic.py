#Function that prints first n harmonic divisor numbers (numbers whose divisors have an integer hm)
import statistics as stat
def printHarmonic(n):
    count = 0
    num = 1
    while(count != n):
        div = []	#to find all divisors
        hm = 0
        for i in range (1, num+1):
            if(num % i == 0):
                div.append(i)
        hm = stat.harmonic_mean(div)
        if(hm == 1 or hm.is_integer()): #is_integer works only on floats
            print("Harmonic Divisor Number {}:".format(count+1), num)
            count+=1
        num += 1
printHarmonic(10)
