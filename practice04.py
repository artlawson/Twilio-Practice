import math
import os
import random
import re
import sys

#return the minimum number of characters needed to make a given
#password a "strong" password with at least 1 upper, 1 lower, 1 special,
#1 number, and length 6
#arguments: n = lengeth of password, 

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    x = False
    y = False
    z = False
    a = False
    app = 0
    if n < 6:
        total = 6-n
    else:
        total = 0
    
    for char in password:
        if char in lower_case:
            x = True
        elif char in upper_case:
            y = True
        elif char in numbers:
            z = True
        elif char in special_characters:
            a = True
    if x==False:
        app+=1
    if y==False:
        app+=1
    if z==False:
        app+=1
    if a==False:
        app+=1
    if app >total:
        total = app
    
    return total
        
        

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
