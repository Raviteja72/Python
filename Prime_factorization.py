# Prime Factorization

import math
n = int(input())
for i in range(n):
    l,r = input().split()
    l=int(l)
    r=int(r)
    pi=[]
    for i in range(2,r+1):
        for j in range(2,int(math.sqrt(i))+1):
            if(i%j == 0):
                break
        else:
            pi.append(i)
    
    #print(pi)
    c=0
    for i in range(l,r+1):
        k=0
        pr=[0]*len(pi)
        
        while(i>1):
            if(k == len(pi)):
                break
            elif(i%pi[k]==0):
                i = i//pi[k]
                pr[k]=pr[k]+1 
            else:
                k=k+1
        #print(pr)   
        if(len(pr)>0 and max(pr)<=1):
            c=c+1
    print("Lucky numbers : ",c)
        
        