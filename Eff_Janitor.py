# Efficient janitor

n = int(input())

l = list(map(float,input().split()))

start=0
end=n-1
t=0
while(start<=end):
    if(l[start]+l[end] <= 3.00):
        t=t+1
        start=start+1 
        end=end-1
    else:
        end=end-1
        t=t+1 
print(t)