import math
import os
import random
import re
import sys
import copy

#choose any three indexes and swap then ABC > BCA > CAB >ABC to see if they correctly can sort the array

# Complete the larrysArray function below.
def larrysArray(A):
    #create sorted version of given array
    #perform swap
    #if the new array doesn't match, try next 3
    B = copy.copy(A) #for comparing to A
    C = copy.copy(A) #for resetting B
    A.sort()
    x=0
    while B!=A:
        print("taco")
        B[x], B[x+1], B[x+2] = B[x+1], B[x+2], B[x] #BCA, CAB, ABC
        if B!=A:
            B[x], B[x+1], B[x+2] = B[x+2], B[x], B[x+1]
            if B!=A:
                B[x], B[x+1], B[x+2] = B[x+2], B[x], B[x+1]
            else:
                return("YES", "so")
                break
        else:
            return "YES"
            break
        x+=1
        B= copy.copy(C)
        if x== len(A)-2:
            return("NO")
            break
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
