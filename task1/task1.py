import sys
import math
import functools

def OpenFile(path):

    try:
        with open(path, "r") as file:
            return file.readlines()
    except:
        return ""

def Percentile(N, percent, key=lambda x:x):

    if not N:
        return None
    k = (len(N)-1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    d0 = key(N[int(f)]) * (c-k)
    d1 = key(N[int(c)]) * (k-f)
    return d0+d1

def CheckRange(checkValue, num1, num2):
    if (num1 < num2):
        return num1 < checkValue < num2
    if (num1 > num2):
        return num2 < checkValue < num1
        
    return False



args = sys.argv
dataFile_path = ""
dataFile = ""
numArray = []

if (len(args) > 1):
    dataFile_path = args[1]

    dataFile = OpenFile(dataFile_path)

    if (dataFile != ""):
        
        for elem in dataFile:
            numArray.append(int(elem.strip()))
            
        numArray.sort()
        
        perc = Percentile(numArray, 0.9)
        med = sum(numArray)/len(numArray)

        result = 0
        
        for elem in numArray:
            if (CheckRange(elem, perc, med)):
                result = result + elem
                
        print (str(result))
        