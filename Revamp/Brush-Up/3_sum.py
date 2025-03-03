nums = [-1,0,1,2,-1,-4]
threeSum = 0
res = []
nums.sort()  #[-4,-1,-1,0,1,2]

for i,a in enumerate(nums):
    if i>0 and a == nums[i-1]:
        continue
    l,r = i+1, len(nums)-1
    while l < r:
        threeSum = a + nums[l] + nums[r]
        if threeSum > 0:
            r -= 1
        elif threeSum < 0:
            l += 1
        else:
            res.append([a,nums[l],nums[r]])
            l += 1
            while l<r and nums[l-1] == nums[l]:
                l += 1
print(res)


