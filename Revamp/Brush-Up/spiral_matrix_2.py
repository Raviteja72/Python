
# ans = []
# val = 0
# st,en = 0,n
# for i in range(n):
#     a = []
#     for j in range(st,en):
#         a.append(j+1)
#         st += 1
#         en += 1
#     ans.append(a)

# a = []
# for i in range(1,n*n+1):
#     a.append(i)
#     if(i%3 == 0):
#         ans.append(a)
#         a = []
# print(ans)

# arr = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(1):
#     for j in range(3):
#         arr[i][j] = 9
# print(arr)


left, right = 0, n
top, bottom = 0, n 
res = [[0]*3 for _ in range(3)]
val = 1
while left < right and top < bottom :
    for i in range(left, right):
        res[top][i] = val
        val += 1
    top += 1
    print("Top row", res)

    for i in range(top, bottom):
        res[i][right-1] = val
        val += 1
    right -= 1
    print("Right Row",res)

    if not (left < right and top < bottom):
        break 

    for i in range(right-1, left-1, -1):
        res[bottom-1][i] = val 
        val += 1
    bottom -= 1
    print("Bottom Row",res)

    for i in range(bottom-1, top-1, -1):
        res[i][left] = val 
        val += 1
    left += 1
    print("Left Row",res)

print(res)
