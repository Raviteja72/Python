'''define a function to check whether a given name is valid or not.
for validation :
a. name should be in uppercase letter , includes space only
b. min length 5 , max length 20
 
if valid , return message as "Name is valid"
otherwise handling an exception with a message {name} is invalid in format'''
import re 

def check(st):
    try:
        # if(re.match(r'^.*[#$%&!*(){}:,-=_+/0-9a-z]',st) == None):
        if(re.match(r'^[A-Z ]{5,20}$',st)):
            return st," is valid"
        else:
            raise Exception 
    except Exception:
        return st," is invalid in format"


# st = "RAVITEJA KARAVADI"
# print(check(st))

class AgeException(Exception):
    pass

def checkExp(l):

    valid,invalid=0,0
    for i in l:
        if(i["age"] >= 18 and i["age"] <= 60):
            valid+=1
        else:
            invalid += 1 
    try :
        if(valid != 0):
            return (
                {"Status":"OK",
                "no. of valid employees":valid,
                "no. of invalid employees":invalid}
            )
        else:
            raise AgeException
    except AgeException:
        return (
            {"Status":"INVALID ",
            "Message":"All employees are invalid"}
        )
        

# n = int(input("Enter no. of employees : "))
# l=[]
# for i in range(n):
#     d = {}
#     d["name"] = input("name: ")
#     d["age"] = int(input("age: "))
#     d["location"] = input("location: ")
#     l.append(d)
# ans = checkExp(l)
# print(ans)

number = 10
ans = ""
if ( number == 0 ):
        print(0)
while ( number ):
    ans += str(number&1)
    number = number >> 1
    
ans = ans[::-1]
print(ans)