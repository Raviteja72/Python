def step():
    st_num = int(input("Enter the starting number:"))
    if(st_num < 0):
        print("Invalid starting number")
    else:
        en_num = int(input("Enter the ending number:"))
        if(en_num <= 0):
            print("Invalid ending number")
        elif(st_num == en_num):
            print("Starting and ending number must not be same")
        else:
            flag = True
            l = []
            step_value = int(input("Enter the step value:"))
            if(step_value == 0):
                print("Invalid step value")
            elif(step_value > 0):
                if(st_num < en_num):
                    if(st_num == 0):
                        for i in range(1,en_num+1,step_value):
                            l.append(i)
                    else:
                        for i in range(st_num,en_num+1,step_value):
                            l.append(i)
                else:
                    print("Invalid step value")
                    flag = False
            else:
                if(st_num > en_num):
                    for i in range(st_num,en_num-1,step_value):
                        l.append(i)
                else:
                    print("Invalid step value")
                    flag = False
            if(flag):
                print(l)
# step()

def makePyramid(n):
    l = []
    for i in range(1,n):
        if(n%i == 0):
            l.append(i)
    # print(l)
    for i in range(len(l)):
        for j in range(i+1):
            print(l[j],end= " ")
        print()

# n = int(input("Enter the number : "))
# makePyramid(n)

def isPerfect(n):
    s=0
    for i in range(1,n):
        if(n%i == 0):
            s+= i
    if(s==n):
        return True 
    else:
        return False  

def findPerfect(lst):
    ans=[]
    for i in lst:
        if(isPerfect(i)):
            ans.append(i)
    if(len(ans)>0):
        print("Perfect numbers : ",ans)
    else:
        print("No perfect numbers are present")

lst = list(map(int,input("Enter list elements : ").split(" ")))
findPerfect(lst)