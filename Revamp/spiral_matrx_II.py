# matrix = []
ans = []
n = 3

a = b = n 
top,bottom,right,left = 0,b-1,a-1,0
ans = [[0]*n for _ in range(n)]
val = 0
while(top <= bottom and left <= right):
    for i in range(left,right+1):
        val += 1
        ans[top][i] = val
    top += 1 

    for i in range(top,bottom+1):
        val += 1
        ans[i][right] = val 
    right -= 1

    if(top <= bottom):
        for i in range(right,left-1,-1):
            val += 1
            ans[bottom][i] = val 
        bottom -= 1
    
    if(left <= right):
        for i in range(bottom,top-1,-1):
            val += 1
            ans[i][left] = val
        left += 1
print(ans)





# for i in range(1,n*n + 1):
#     ans.append(i)
#     if(len(ans)%n == 0):
#         matrix.append(ans)
#         ans = []
# # print(matrix)

# res = []
# a,b = len(matrix),len(matrix[0])
# top,bottom,left,right = 0,a-1,0,b-1

# while(left <= right and top <= bottom):
#     for i in range(left,right+1):
#         res.append(matrix[top][i])
#     top += 1

#     for i in range(top,bottom+1):
#         res.append(matrix[i][right])
#     right -= 1

#     if(top <= bottom):
#         for i in range(right,left-1,-1):
#             res.append(matrix[bottom][i])
#         bottom -= 1
    
#     if(left <= right):
#         for i in range(bottom,top-1,-1):
#             res.append(matrix[i][left])
#         left += 1
    
# print(res)

# res_2 = []
# ans = []
# for i in range(len(res)):
#     res_2.append(res[i])
#     if(len(res_2)%3 == 0):
#         ans.append(res_2)
#         res_2 = []

# print(ans)

    