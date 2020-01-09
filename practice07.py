import os
import sys

#
# Complete the timeConversion function below.


#convert given regular time to military time 
#format "HH:MM:SSAM"
#
def timeConversion(s):
    #check to see if it is am or pm
    #if pm, add 12 and return
    #if am return without the am
    x = 12
    if s[-2] == "P":
        if s[0:2] == "12":
            pass
        else:
            x+=int(s[0:2])
            x=str(x)
            for i in s[2:]:
                x+=i
            #s[0:1] = str(int(s[0:1]) + 12)
        return x[0:-2]
    else:
        if s[0:2] == "12":
            x="00"
        else:
            x+=int(s[0:2])
        for i in s[3:]:
            x+=i
        return x[0:-2]
        
    #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
