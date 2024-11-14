arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
m,n = len(arr),len(arr[0])
top,bottom,right,left = 0,m-1,n-1,0
ans = []
while(top <= bottom and left <= right):
    for i in range(left,right+1):
        ans.append(arr[top][i])
    top += 1 

    for i in range(top,bottom+1):
        ans.append(arr[i][right])
    right -= 1

    if(top <= bottom):
        for i in range(right,left-1,-1):
            ans.append(arr[bottom][i])
        bottom -= 1
    
    if(left <= right):
        for i in range(bottom,top-1,-1):
            ans.append(arr[i][left])
        left += 1
print(ans)


    


















# res = []
# r,c = 0,0 
# di = 0 
# m = len(arr)
# n = len(arr[0])
# seen = [[0] * n for _ in range(m)]
# dr,dc = [0,1,0,-1],[1,0,-1,0]

# for i in range(m*n):
#     res.append(arr[r][c])
#     seen[r][c] = 1

#     newR,newC = r+dr[di],c+dc[di]
#     # print(seen[newR][newC])

#     if(0 <= newR < m and 0 <= newC < n and seen[newR][newC] != 1):
#         r,c = newR,newC 
#     else:
#         di = (di+1)%4
#         r += dr[di]
#         c += dc[di]
# print(res)