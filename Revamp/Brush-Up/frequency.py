arr = [1,2,34,6,8,1,3,5,8,2,2,34,5,1,2,2,3,45,7,8,9,4,45,6,6,89]

d = {}

for i in arr:
    if i not in d:
        d[i] = 1 
    else:
        d[i] += 1
print(d)