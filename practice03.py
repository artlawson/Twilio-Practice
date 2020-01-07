import math
import os
import random
import re
import sys

#given a list of integers, determine how many pairs there are

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #sort list
    #if x = x+1, delete both and add one
    ar.sort()
    print(ar)
    z = -1
    
    num = 0
    while n - 1> z:
        z+=1
        x = ar[z]
        if x!= ar[-1]:
            y = ar[z+1]
        else:
            y = 318318318
        if x == y:
            print("x", z)
            num+=1
            del x
            del y
        else:
            del x
    return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
