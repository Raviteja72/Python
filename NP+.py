# Wipro Q-1
from math import sqrt
n=input()
s=0
for i in n:
    if(int(i) == 1):
        s=s+1 
        continue
    for j in range(2,int(sqrt(int(i))+1)):
        if(int(i)%j != 0):
            #print("P : ",i)
            break
    else:
        #print("NP = ",i)
        s=s+int(i)
        
print(s)
        
