# arr = [2,-3,2,4] # 8
arr = [2,-5,-2,-4,3]

prefix = suffix = 1
maxy = float('-inf')

for i in range(len(arr)):
    if prefix == 0: prefix = 1
    if suffix == 0: suffix = 1

    prefix *= arr[i]
    suffix *= arr[len(arr)-i-1]

    maxy = max(maxy, prefix, suffix)

print(maxy)
