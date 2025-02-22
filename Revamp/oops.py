

# class Dog:
#     dogname = "Shepard"

#     def __init__(self,breed):
#         self.breed = breed 
#         Dog.dogname += " - Dog"
    
#     def display(self):
#         print(self.breed," - ",Dog.dogname)

# d = Dog("Puppy")
# print(Dog.dogname)
# print(d.__class__.dogname)
# d.display()




# a = input()
# try:
#     if(float(a)):
#         print(a," is digit")
#     else:
#         raise Exception
# except:
#     print(a," is alphabet")


# name = input()
# key = int(input())
# ans = ""
# for i in name:
#     if(i.isalpha()):
#         if(ord(i)+key > 120):
#             ans += chr(ord(i)+key - 26)
#         else:
#             ans += chr(ord(i)+key)
#     else:
#         ans += i 
# print(ans)

# print(eval("2+4"))
# from collections import OrderedDict 
# d = {2:'anmisha',9:'bebra',5:'eye',4:'infy'}
# dic1 = OrderedDict(sorted(d.items()))
# print(dic1)

# arr={}
# import operator
# sorted_values = sorted(d.items(), key=operator.itemgetter(0), reverse=True)
# for k,v in sorted_values:
#     arr[k] = v
# print(arr)

# ans={}
# import operator 
# sorted_values = sorted(d.items(), key=operator.itemgetter(0))
# for k,v in sorted_values:
#     ans[k] = v 
# print(ans)

# arr = "Raviteja"
# # print(arr[::])

# d = {}
# if len(d) == 0:
    # print("Zero")

def is_palindrome(sentence):
    arr = ""
    for i in sentence:
        if(i.isalpha()):
            arr += i.lower()
    if(arr == arr[::-1]):
        return True
    else:
        return False
    
# re.findall(r"\b\w+\b",i)
    
# sentence = input("Enter a sentence:")
# ans = is_palindrome(sentence)
# if(ans):
#     print(sentence,"is palindrome")
# else:
#     print(sentence,"is not a palindrome")


def calculate_days(from_date,to_date):
    from_day,from_mon = from_date.split("/")
    to_day,to_mon = to_date.split("/")
    days = int(to_day) - int(from_day) + (int(to_mon)-int(from_mon))*30
    return days 

def calculate_total_amount(customer_name,room_type,no_of_days):
    rent=0 
    d={}
    if(room_type == "Single"):
        if(no_of_days <= 3):
            rent = 3300 - 3300*0.1
        else:
            rent = 3300 - 3300*0.15
    elif(room_type == "Double"):
        if(no_of_days <= 3):
            rent = 4000 - 4000*0.1
        else:
            rent = 4000 - 4000*0.17
    else:
        if(no_of_days <= 3):
            rent = 4500 - 4500 * 0.1 
        else:
            rent = 4500 - 4500*0.2 
    d["Customer Name"] = customer_name
    d["No of days"] = no_of_days
    d["Total amount"] = rent 
    return d 
    
# st = input()
# arr = st.split(":")
# from_date,to_date = arr[3],arr[4]
# days = calculate_days(from_date,to_date)
# tot_amount = calculate_total_amount(arr[1],arr[2],days)
# print("Customer Name:",tot_amount['Customer Name'])
# print("No of days:",tot_amount['No of days'])
# print("Total amount:",tot_amount['Total amount'])


def check_scholarship(string_1,string_2):
    ans = []
    list_1 = string_1.split(",")
    list_2 = string_2.split(",")
    if(len(list_1) < len(list_2)):
        return "Invalid data"
    else:
        for i in list_1:
            if i not in list_2:
                ans.append(i)
        if(len(ans)==0):
            return "All students have scholarships"
        else:
            return ans 

string_1 = input()
string_2 = input()
val = check_scholarship(string_1,string_2)
if(type(val)==list):
    print("Students without scholarships:",end="")
    print(*val,sep=",") 
else:
    print(val)

