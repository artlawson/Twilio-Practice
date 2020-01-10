import math
import os
import random
import re
import sys

#return the time in words

# Complete the timeInWords function below.
def timeInWords(h, m):
    time = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15 : "quarter", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20 : "twenty", 21 : "twenty-one", 22: "twenty-two", 23: "twenty-three", 24: "twenty-four", 25: "twenty-five", 26: "twenty-six", 27: "twenty-seven", 28: "twenty-eight", 29: "twenty-nine", 30: "half"}
    x = h+1
    if h ==12:
        x = 1
#determine if it is before half mark
    
    if m==0:
        return time[h] + " o' clock"
    elif m==15:
        return time[m] + " past " + time[h]
    elif m <= 30 and m > 0:
        return time[m] + " minutes past " + time[h]
    elif m==45:
        return time[m] + " to " + time[x]
    else:
        return time[60 - m] + " minutes to " + time[x]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
