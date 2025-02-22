# st = "AbcD"
# if(re.match(r"^[A-Za-z]+$",st)):
#     print("Only alphabets")
# else:
#     print("Invalid input")

# st = "1A12B"
# # if(re.search(r"[A-Za-z]+",st) and re.search(r"[0-9]+",st)):
# if(re.match(r"^(?=.*[0-9])(?=.*[A-Za-z])[A-Za-z0-9]+$",st)):
#     print("Atleast 1 alphabet and 1 digit present")
# else:
#     print("Invalid Input")

# vals = re.findall(r"[^0-9]",st)
# print(vals)

def check(name):
    if(re.match(r"^[A-Z ]{5,20}$",name)):
        return "valid"
    else:
        return "Invalid"
# print(check("RAVITEJA KARAVADI"))_

#@! 
# l=6 
# 1a 1d 1spe 
# w >6 <10 
# strong > 10

# if re.findall(r'(?=.*[A-Za-z0-9])(?=.*[@#!])[A-Za-z0-9@#!]{6,}$',s):

def check_str(pwd):
    if(re.match(r"^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[#@!])([A-Za-z0-9@#!]+){7,10}$",pwd)):
        if(len(pwd)>6 and len(pwd)<10):
            print("Weak password")
        else:
            print("Strong password")
    else:
        print("Invalid password")
    
# check_str("R@v!tej12rt")

# st = "INS-123"
# if(re.match(r"^INS-[0-9]{3}$",st)):
#     print("Checked?")

def check_email(email):
    if(re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$",email)):
        print("Email Checked")
    else:
        print("Invalid Email")

# check_email("72@gmil.com")





