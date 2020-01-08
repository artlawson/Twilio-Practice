import math
import os
import random
import re
import sys

############ goal: return the length of the largest possible subset
############ in which the sum of any two numbers in the subset is not divisible by a given k

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    sat = []
    #iterate through and add each i to each other number
    #if the sum !| k, add to that number's list
    #we should run it on that number's list too
    #record the len of that number's list, if it is longer than
    #the previous long, replace the current
    #helper function?
    x = 0
    sat.append(s[0])
    for i in s:
        x+=1
        for j in range(x, len(s)):
            q = s[j]
            if (i+q) % k !=0:
                if q not in sat:
                    sat.append(q)
    #print(sat)

    ####first half of code works for really small basic examples
    ####the second half is supposed to weed out in the general list things that don't work with each other (instead of just the first element)

    y = 0
    for a in sat:
        y+=1
        for t in range(y, len(sat)):
            q = sat[t]
            if (a+q) % k ==0:
                sat.remove(q)
    return len(sat)

            
    return len(sat)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
