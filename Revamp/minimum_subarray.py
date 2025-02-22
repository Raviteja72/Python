# arr = list(map(int, input("Array : ").split(",")))
# res,maxi_end = arr[0],arr[0]

# for i in range(1, len(arr)):
#     # cur_sum = arr[i]

#     maxi_end = min(arr[i]+maxi_end, arr[i])

#     res = min(res, maxi_end)

# print(res)

arr = list(map(int,input().split(",")))
st,en,poi = 0,0,0
curr_sum,min_so_far = 0,arr[0]
for i in range(len(arr)):
    curr_sum += arr[i]

    if(min_so_far > curr_sum):
        min_so_far = curr_sum
        # st=poi
         
    if(curr_sum > 0):
        curr_sum = 0
        # poi = i+1
        # en=i 
print("Minimum Sum of Subarray is : ",min_so_far)