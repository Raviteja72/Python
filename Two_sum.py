arr = [2,7,11,15]
target = 9
# Without sorting
seen = {}
for i,n in enumerate(arr):
    diff = target - n 
    if diff in seen:
        print('Ans - ',seen[diff],i)
        break
    seen[n] = i
    # print(seen)
    
#With Sorting 
# arr = [15,2,11,7,1]
# arr.sort()
# target = 9
# st,en = 0,len(arr)-1 
# while (st < en):
#     curSum = arr[st] + arr[en]
#     if(curSum < target):
#         st += 1 
#     elif(curSum > target):
#         en -= 1 
#     else:
#         print(st,en)
#         break





# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         # print(i,j)
#         if(arr[i] + arr[j] == target):
#             print(i,j)
