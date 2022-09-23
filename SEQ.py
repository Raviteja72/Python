# Largest sum of sub-arrays
# increasing
# decreasing


n = int(input())

a = list(map(int,input().split()))

start=0
end=start+1 
curr_diff=0
max_diff=0
for i in range(n-1):
    if(a[end]<a[end-1]):
        curr_diff = end-start
        max_diff = max(curr_diff,max_diff)
        pos = i+1
        end=end+1 
    else:
        curr_diff = 0
        start=end 
        end=end+1
     

#print(max_diff)
val = pos-max_diff
print("Largest decreasing sequence : ",a[val:i+1])
 
start=0
end=start+1 
curr_diff=0
max_diff=0
s=""
for i in range(n-1):
    if(a[end]>a[end-1]):
        curr_diff = end-start
        if(curr_diff > max_diff):
            s=s+str(end-1)
            en=end 
            #print(st,en)
        max_diff = max(curr_diff,max_diff)
        pos = i+1
        end=end+1 
    else:
        curr_diff = 0
        start=end 
        end=end+1
        

print("Largest increasing sequence : ",a[int(s[0]):en+1])
        