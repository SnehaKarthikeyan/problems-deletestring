Coding:
  
def checkEmpty(input1, pattern):  
    if len(input1)== 0 and len(pattern)== 0:  
         return 'YES'
    if len(pattern)== 0:  
         return 'YES'
    while (len(input1) != 0):  
        index = input1.find(pattern)  
        if (index ==(-1)):  
          return 'NO'
        input1 = input1[0:index] + input1[index + len(pattern):]               
    return 'YES'
input1=input()
pattern =input()
print (checkEmpty(input1, pattern)) 
