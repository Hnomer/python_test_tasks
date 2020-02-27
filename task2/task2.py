import sys
import json
import re
import math

def OpenFile(path):

    try:
        with open(path, "r") as file:
            return file.readlines()
    except:
        return ""
        
def Dotproduct(vector1, vector2):
    return sum((a*b) for a, b in zip(vector1, vector2))

def Length(vector):
    return math.sqrt(Dotproduct(vector, vector))

def Angle(vector1, vector2):
    return math.acos(Dotproduct(vector1, vector2) / (Length(vector1) * Length(vector2)))
  
def Distance(point1, point2):

    return math.sqrt(((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2) + ((point2[2] - point1[2]) ** 2))
    
def AngleByThreePoints(point1, point2, point3):
    
    vector1 = []
    vector2 = []
    
    vector1.append(point2[0] - point1[0])
    vector1.append(point2[1] - point1[1])
    vector1.append(point2[2] - point1[2])
    
    vector2.append(point2[0] - point3[0])
    vector2.append(point2[1] - point3[1])
    vector2.append(point2[2] - point3[2])
    
    return math.degrees(Angle(vector1, vector2))


def simi_aaa(a1, a2):              
    a1 = [float(i) for i in a1] 
    a2 = [float(i) for i in a2] 
    a1.sort() 
    a2.sort() 

    if a1[0] == a2[0] and a1[1] == a2[1] and a1[2] == a2[2]: 
        return 1
    return 0


def simi_sas(s1, s2, a1, a2):  
      
    s1 = [float(i) for i in s1] 
    s2 = [float(i) for i in s2] 
    a1 = [float(i) for i in a1] 
    a2 = [float(i) for i in a2] 
    
    s1.sort() 
    s2.sort() 
    a1.sort() 
    a2.sort() 

    if s1[0] / s2[0] == s1[1] / s2[1]: 

        if a1[2] == a2[2]:          
            return 1

    if s1[1] / s2[1] == s1[2] / s2[2]: 
        if a1[0] == a2[0]: 
            return 1

    if s1[2] / s2[2] == s1[0] / s2[0]: 
        if a1[1] == a2[1]: 
            return 1

    return 0

def simi_sss(s1, s2):  
      
    s1 = [float(i) for i in s1] 
    s2 = [float(i) for i in s2]  
    s1.sort() 
    s2.sort()  

    if(s1[0] / s2[0] == s1[1] / s2[1]  
        and s1[1] / s2[1] == s1[2] / s2[2]  
        and s1[2] / s2[2] == s1[0] / s2[0]): 
        return 1
      
    return 0
    

args = sys.argv
dataFile_path = ""
dataFile = ""

if (len(args) > 1):

    dataFile_path = args[1]

dataFile = OpenFile(dataFile_path)

if (dataFile != ""):
    
    jsonString = re.sub(r'([a-z]+[0-9])', r'"\1"', dataFile[0])
    jsonString = re.sub(r'([ABC])', r'"\1"', jsonString)

    jsonData = json.loads(jsonString)
    
    t1 = jsonData["triangle1"]
    t2 = jsonData["triangle2"]
    
    s1 = [Distance(t1["A"], t1["B"]), Distance(t1["B"], t1["C"]), Distance(t1["A"], t1["C"])]
    s2 = [Distance(t2["A"], t2["B"]), Distance(t2["B"], t2["C"]), Distance(t2["A"], t2["C"])]
    
    a1 = []
    a2 = []
    
    a1.append(AngleByThreePoints(t1["A"], t1["B"], t1["C"]))
    a1.append(AngleByThreePoints(t1["B"], t1["C"], t1["A"]))
    a1.append(AngleByThreePoints(t1["C"], t1["A"], t1["B"]))
    
    a2.append(AngleByThreePoints(t2["A"], t2["B"], t2["C"]))
    a2.append(AngleByThreePoints(t2["B"], t2["C"], t2["A"]))
    a2.append(AngleByThreePoints(t2["C"], t2["A"], t2["B"]))
    

    aaa = simi_aaa(a1, a2)  

    sss = simi_sss(s1, s2)  

    sas = simi_sas(s1, s2, a1, a2)
    
    if (aaa or sss or sas):
        print("YES")
    else:
        print("NO")
    

input()
