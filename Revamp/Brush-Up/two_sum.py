nums = list(map(int, input().split(",")))
target = 9
# nums.sort()
# st,en = 0,len(nums)-1
# val = 0
# for i in range(len(nums)-1):
#     val = nums[st]+nums[en]
#     if(val == target):
#         break
#     elif(val > target):
#         en = en-1
#     else:
#         st = st+1
# print(st,en)


seen = {}
for i,n in enumerate(nums):
    diff = target-n 
    if diff in seen:
       print([i, nums.index[diff]])
    seen[n] = i





