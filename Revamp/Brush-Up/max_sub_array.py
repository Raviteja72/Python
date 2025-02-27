arr = [2,3,4,-1,-5,1]

currSum = 0
maxy = float('-inf')

for i in range(len(arr)):
    currSum += arr[i]
    maxy = max(currSum, maxy)

    if currSum < 0:
        currSum = 0
    # print("CS : ",currSum," Max : ",maxy)
print(maxy)