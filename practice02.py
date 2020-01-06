import math
import os
import random
import re
import sys

#####
#return min and max of 4/5 given digits in an 
######

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    baby = 0
    mega = 0
    arr.sort()
    for i in range(0, len(arr) - 1):
        baby+=arr[i]
    for k in range(1, len(arr)):
        mega+=arr[k]
    print(baby, mega)

    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
