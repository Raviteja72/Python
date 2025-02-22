


import re
def vals(n):
    try:
        if(re.match(r".*[A-Za-z]",str(n))):
            raise Exception("data is improper format")
        elif(n<=0):
            raise Exception("data should be positive")
        else:
            for i in range(2,n//2 +1):
                if(n%i == 0):
                    break
            else:
                return n 
    except Exception as e:
        print(e)

def val(n):
    for i in range(2,n//2 +1):
        if(n%i == 0):
            break
    else:
        return n
    return

# n = -1
# val(n)

def getPrimes(lst):
    ans=[]
    for i in lst:
        for j in range(2,i//2 + 1):
            if(i%j == 0):
                break 
        else:
            opt = val(i)
            try:
                if(opt and opt!= 1):
                    ans.append(opt)
            except:
                pass
    try:
        if(len(ans)>0):
            print("Primes are : ",ans)
        else:
            raise Exception
    except:
        print("Prime number not found")
    return

# getPrimes([1,12,9,7,3,5,24])

def checkPrime():
    try:
        n = int(input('Enter number:'))
        if (n<=0):
              raise Exception('Number should be positive and non zero')
        flag=True
        for i in range(2,n):
              if (n%i==0):
                   flag=False
                   break
        if(flag):
            print(n, ' is prime number')
        else:
             print(n , ' is not prime number')
   
    except ValueError as e:
         print('Number not in proper format')    
    except Exception as e:
         print(e)
 
# checkPrime()

def getPrimes(listNumbers):
     list=[]
     for n in listNumbers:
          flag=True
          for i in range(2,n):
              if (n%i==0):
                   flag=False
                   break
          if(flag):
            list.append(n)
     if(len(list)==0):
        raise Exception('No prime numbers')
     else:
        return list
   
 
# try:
#     list = getPrimes([12,24])
#     print(list)
# except Exception as e:
#     print(e)


def convertString(st):
    ans = ""
    for i in st:
        if(i.isupper()):
            if(i=='Z'):
                ans += 'A'
            else:
                ans += chr(ord(i)+1)
        else:
            raise Exception("improper data")
    return ans 

# try:
#     val = convertString("AXYZP")
#     print(val)
# except Exception as e:
#     print(e)

n = 126
print(hex(n)[2:])



if n == 0:
    print(0)
else:
    hex_digits = "0123456789abcdef"
    hex_val = ""
    while n > 0:
        remainder = n % 16
        hex_val = hex_digits[remainder] + hex_val
        n = n // 16
print(hex_val)

print(oct(10))

def adder(x):
    def sums(y):
        return x+y 
    return sums

adds = adder(10)
print(adds(20))


def A(func):
    def B():
        print("Inside B before func")
        func()
        print("Inside B after func")
    return B 

def func_used():
    print("Inside func used")

val = A(func_used)
val()

import re 
val = "krtproperty72@.com"
if(re.match(r"(?=.*@gmail.com)",val) or re.match(r"(?=.*@hotmail.com)",val)):
# if val in ["@gmail.com","@hotmail.com"]:
    print(True)