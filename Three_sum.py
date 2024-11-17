arr = [-2,0,1,1,2]

n = len(arr)
ans = []
for i in range(n):
    if(i>0 and arr[i] == arr[i-1]):
        continue 
    l = i+1
    r = n-1 
    while(l<r):
        cs = arr[i]+arr[l]+arr[r]
        if(cs == 0):
            ans.append([arr[i],arr[l],arr[r]])
            l+=1
            while(l<r and arr[l] == arr[l-1]):
                l += 1
        elif(cs > 0):
            r-=1
        else:
            l += 1
print(ans)


