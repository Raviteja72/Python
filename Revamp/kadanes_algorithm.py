# arr = list(map(int,input().split(",")))
# st,en,poi = 0,0,0
# curr_sum,max_so_far = 0,arr[0]
# for i in range(len(arr)):
#     curr_sum += arr[i]

#     if(max_so_far < curr_sum):
#         max_so_far = curr_sum
#         st=poi
#         en=i  
#     if(curr_sum < 0):
#         curr_sum = 0
#         poi = i+1 
# print("Maximum Sum of Subarray is : ",max_so_far)

l = [[0,0,0],[0,0,0]]
ans = []
val = 0
for i in range(len(l)-1):
    if (l[val][0],l[val][1],l[val][2] == l[i+1][0],l[i+1][1],l[i+1][2]):
        ans.append([l[i][0],l[i][1],l[i][2]])
        # i += 1
print(ans)

