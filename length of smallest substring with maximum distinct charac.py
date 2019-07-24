char = 256
str = input()
def maxchar(str, n):
    count = [0] * char 
    for i in range(n): 
        count[ord(str[i])] += 1
    maxdis = 0
    for i in range(char): 
        if (count[i] != 0): 
            maxdis += 1    
    return maxdis
def smallstr_maxChar(str):   
    n = len(str)      
    maxdis = maxchar(str, n) 
    minl = n    
    for i in range(n): 
        for j in range(n): 
            subs = str[i:j] 
            subs_lenght = len(subs) 
            sub_distinct_char = maxchar(subs,subs_lenght)
            if (subs_lenght < minl and 
                maxdis == sub_distinct_char): 
                minl = subs_lenght 
    return minl 
l = smallstr_maxChar(str)
print( "The length of the smallest substring consisting of maximum distinct characters :", l)

      
   
