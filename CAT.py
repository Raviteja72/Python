# Minimum ATM withdrawls
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
m=int(input())  # Main Sum
T=sum(l)-m  # Target
curr_sum,max_len,curr_len = 0,0,0
i,j=0,1 
while(i<n and j<n):
    #print("HI")
    curr_sum = sum(l[i:j+1])
    print(curr_sum)
    if(curr_sum < T):
        j=j+1
    elif(curr_sum > T):
        i=i+1 
    else:
        curr_len = j-i+1 
        max_len = max(max_len,curr_len)
        j=j+1 
        
if(max_len == 0):
    if(sum(l) == m):
        print(n)
    else:
        print('-1')
else:
    print(n-max_len)
        
    
    
    