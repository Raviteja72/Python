# n = int(input("How many number? : "))
# l=[]
# for i in range(n):
#     while(True):
#         val = int(input("Enter number for position[{}]: ".format(i+1)))
#         if(val >= 0):
#             break 
#     l.append(val)

# l.sort()
# print("Data are : ",*l,sep=" ")
# print("Sum : ",sum(l),"\nMax : ",max(l),"\nMin : ",min(l))

#@! 
# l=6 
# 1a 1d 1spe 
# w >6 <10 
# strong > 10
import re
def checkString(st):
    flag = False
    if(len(st) >= 6): # /^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$/
        # val = re.findall("/^(?=.*[0-9]+)/",st)
        # print(val)
        if(re.search("[#@!]",st) != None and re.search("[A-Za-z]",st) != None and re.search("[0-9]",st) != None):
            flag = True 
    
        if(flag):
            if(len(st)>=6 and len(st)<=10):
                return "valid but weak"
            elif(len(st)>10):
                return "valid and strong"
        else:
            return "invalid"
    else:
            return "invalid"

# st = "12345ar@"
# checkString(st)

def pan(st):
     val = re.match("[A-Z]{5}[0-9]{4}[A-Z]",st)
     if(val):
          return True
     else:
        return False
    #  print(val)
# val = pan("EVOPK7406K")
# if(val):
#     print("Valid PAN")
# else:
#     print("Invalid PAN")


import re
def password(s):
    if re.findall(r'(?=.*[A-Za-z0-9])(?=.*[@#!])[A-Za-z0-9@#!]{6,}$',s):
        if len(s)>6 and len(s)<10:
            return f"Weak Password"
        elif len(s)>10:
            return f"Strong Password"    
    else:
        return f"Invalid Password"
       
s=input("Enter the password:")
print(password(s))  