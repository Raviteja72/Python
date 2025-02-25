arr = [2,7,11,15]
# array is already sorted 
target = 9 

l,r = 0,len(arr)-1
for i in range(len(arr)):
    val = arr[l] + arr[r]
    if(val == target):
        print([l+1,r+1])
        break
    elif(val > 0):
        r -= 1
    else:
        l += 1
