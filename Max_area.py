# max area

n = list(map(int,input().split()))


start=0
end=len(n)-1
max_area=0
while(start<end):
    area=(end-start)*min(n[start],n[end])
    max_area=max(area,max_area)
    #print(max_area)
    if(n[start]<n[end]):
        start=start+1 
    else:
        end=end-1
print(max_area)