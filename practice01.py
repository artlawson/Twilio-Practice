import math
import os
import random
import re
import sys


#a given string is valid if all letters occur the same number of times
# or if removing 1 character makes the rest = frequency
def isValid(s):
    bank = {}
    pie = []
    hasBeen = 0
    tim = "YES"
    #use dictionary to keep track of number of times each string is used
    #if all of the frequencies are =, it is valid
    # if all frequencies are = + 1, it is also valid
    for letter in s:
        if letter not in bank:
            bank[letter] = 1
        else:
            bank[letter]+= 1
        pie.append(bank[letter])
    while hasBeen < 2:
        for num in range(0, len(pie) - 1):
            x = abs(pie[num] - pie[num + 1])
            if x > 1:
                tim = "NO"
                break
            elif x == 1:
                if hasBeen == 1:
                    hasBeen = 318
                    tim = "NO"
                    break

                hasBeen +=1

        
    print(tim)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
