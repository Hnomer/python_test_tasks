import sys

def Match(second, first): 

    if (len(second) == 0 and len(first) == 0): 
        return True

    if (len(second) > 1 and second[0] == '*' and  len(first) == 0): 
        return False

    if ((len(second) != 0 and len(first) != 0 and second[0] == first[0])): 
        return Match(second[1:],first[1:]); 

    if (len(second) != 0 and second[0] == '*'): 
        return Match(second[1:],first) or Match(second,first[1:]) 

    return False

args = sys.argv

if (len(args) > 2):
    
    string1 = args[1]
    string2 = args[2]
    
    if Match(string2, string1): 
        print ("OK")
    else: 
        print ("KO")

input()