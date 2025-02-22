import re 
from sympy import *
from collections import Counter

def is_alliterative(sentence):
    words = sentence.split(" ")
    vowels = ["a","e","i","o","u"]
    ans=set()
    # print(words)
    if(len(words) < 2):
        return False 
    elif(words[0].lower() in vowels):
        # print(words)
        return False
    else:
        for word in words:
            ans.add(word[0].lower())
        # print(ans)
        if(len(ans)==1):
            return True 
        else:
            return False
        

# st = input("Enter the sentence to be validated for alliteration")
# st = "Ann sells sea shells"
# if(is_alliterative(st)):
#     print("The sentence is alliterative")
# else:
#     print("The sentence is not alliterative")

def find_relationship(name1,name2):
    tot_len = len((name1+name2).replace(" ",""))
    val = tot_len%6 
    if(val == 0): return "Soulmates"
    elif(val == 1): return "Collegues"
    elif(val == 2): return "Friends"
    elif(val == 3): return "Good friends"
    elif(val == 4): return "Best friends"
    elif(val == 5): return "Close friends"

# name1 = input("Enter the name 1:")
# name2 = input("Enter the name 2:")
# print(find_relationship(name1,name2))

def is_palindrome(sentence):
    arr = sentence.split(" ")
    rev = ' '.join(arr[::-1])
    if(sentence == rev):
        return "Palindrome"
    else:
        return "Not Palindrome"

# print(is_palindrome("Liril mom Liril"))

def generate_status(bp_level):
    val = bp_level.split("/")
    systolic = int(val[0])
    diastolic = int(val[1])
    if(systolic<90 and diastolic<60): return "Low BP"
    elif((systolic>=90 and systolic<=120) and (diastolic>=60 and diastolic<=80)):
        return "Normal"
    elif((systolic>=121 and systolic<=140) and (diastolic>=81 and diastolic<=90)):
        return "Pre-High BP"
    elif((systolic>=141 and systolic<=190) and (diastolic>=91 and diastolic<=100)):
        return "High BP"
    elif(systolic>190 and diastolic>100):
        return "Hyper Tension"
    else:
        return "Invalid Input"
    
# val = input("Enter the BP level:\n")
# print(generate_status(val))

def calculate_discount(st):
    arr = st.split(":")
    vals = [int(i) for i in arr[0]]
    if(arr[1] == "2BHK"):
        if(sum(vals)%2 != 0):
            return 3900000*0.04
        else:
            return 3700000*0.05
    else:
        if(sum(vals)%2 != 0):
            return 5100000*0.08
        else:
            return 4900000*0.07
        
# print("{:.1f}".format(calculate_discount("435:3BHK")))

def find_lucky_number(dob):
    try:
        arr = dob.split("/")
        date = int(arr[0])
        month = int(arr[1])
        year = int(arr[2])
        if(date > 0 and date<32):
            if(month>0 and month<13):
                if(len(arr[2]) == 4 and year<2023):
                    ans = date+month+year
                else:
                    return "Invalid format"
            else:
                return "Invalid format"
        else:
            return "Invalid format"
        org=0
        r=0
        while(ans != 0):
            r = ans%10 
            org += r 
            ans = ans//10
        return org 
    except:
        return "Invalid format"
    

# val = find_lucky_number("33/14/2999")
# if(val != "Invalid format"):
#     print("The lucky number is ",val)
# else:
#     print(val)

def check_number(vehicle_number):
    if(len(vehicle_number)==10):
        org = 0
        val = vehicle_number[-4:]
        ans = [int(i) for i in val]
        if(sum(ans)%2 != 0):
            for i in range(1,len(ans),2):
                org += ans[i]
        else:
            for i in range(0,len(ans),2):
                org += ans[i]
        # print(ans)
        return "Your discount percentage is {}".format(org)
            
    else:
        return "Invalid vehicle number"

# print(check_number("TN43AD1311"))

def find_exam_result(correct,incorrect):
    val = correct+incorrect
    if(val==120):
        percentage =((correct*2 + incorrect*-1)/120)*100
        if(percentage >= 75):
            return "A"
        elif(percentage>=60 and percentage<75):
            return "B"
        elif(percentage>=50 and percentage<60):
            return "C"
        else:
            return "D"
    else:
        return "Invalid number of questions"

# correct = int(input("Enter the count of correct answers:"))
# incorrect = int(input("Enter the count of incorrect answers:"))
# grade = find_exam_result(correct,incorrect)
# lst = ['A','B','C']
# if(len(grade) > 1):
#     print(grade)
# elif(grade not in lst):
#     print("Sorry! You have failed")
# else:
#     print("You have received",grade,"grade")


def generate_code(product_details):
    product_code = ""
    product_name,destination,month,year = product_details.split(":")
    if(len(product_name) and len(destination) > 3) and ((int(month)>0 and int(month)<13) and len(year)==4):
            if(len(product_name)%2 != 0):
                product_code += product_name[:3].upper()
            else:
                product_code += product_name[-3:].upper()
            product_code += '/'+(destination[0]+destination[-1]).upper()
            product_code += '/'+month+year[-2:]
    else:
        product_code += "Invalid product details"
    return product_code

# lst = input("Enter the details:\n")
# print(generate_code(lst))

def replace_word(sentence,word):
    if word.lower() in sentence.lower():
        return sentence.lower().replace(word.lower(),"*"*len(word))
    else:
        return "The given word is not found in the sentence"

# sentence = input("Enter the sentence:\n")
# word = input("Enter the word:\n")
# print(replace_word(sentence,word))

def generate_secret_key(name):
    ans=""
    # if(name.isalpha() and (len(name)>1 and len(name)<11)):
    if(re.match(r"^[A-Za-z]+$",name) and (len(name)>1 and len(name)<11)):
        ans += name.lower()
        res = [ord(i) for i in ans]
        return chr(int(sum(res)/len(res)))
    else:
        return "Invalid Input"
    
# name = input("Enter the name:")
# print(generate_secret_key(name))

def create_ratings(input_string):
    lst = input_string.split(",")
    d={}
    for i in lst:
        arr = i.split(":")
        d[arr[0]] = float(arr[1])
    return d 

def count_ratings(rating_dict):
    less_5,above_5=[],[]
    for k,v in rating_dict.items():
        if(v<=5):
            less_5.append(k)
        else:
            above_5.append(k)
    if(len(less_5)==0):
        less_5 = "Nil"
    elif(len(above_5)==0):
        above_5 = "Nil"
    return less_5,above_5

vals = input("Enter the ratings (as comma-separated values):")
ans = create_ratings(vals)
less_5,above_5 = count_ratings(ans)
# print(re)
print("The list of trainers with ratings between 0-5:",less_5)
print("The list of trainers with ratings between 6 and above:",above_5)

def calculate_score(participants_list):
    arr=[]
    d={}
    for i in participants_list:
        arr = i.split(":")
        ans = [int(i) for i in arr[1:]]
        d[arr[0]] = int(sum(ans)/len(ans))
    return d 

def filter_participants(participants_dictionary,pass_score):
    ans=[]
    for k,v in participants_dictionary.items():
        if(v >= pass_score):
            ans.append(k)
    return ans 

# n = int(input("Enter the no. of participants:"))
# print("Enter the details:")
# ans=[]
# for i in range(n):
#     ans.append(input())
# vals = calculate_score(ans)
# pass_score = int(input("Enter the pass score to select next level:"))
# res = filter_participants(vals,pass_score)
# if(len(res) != 0):
#     print("Next level selected participants are:")
#     for i in res:
#         print(i)
# else:
#     print("No one selected")

def calculate_days(from_date,to_date):
    from_day,from_mon = from_date.split("/")
    to_day,to_mon = to_date.split("/")
    # print(from_day,to_day,from_mon,to_mon)
    days = int(to_day) - int(from_day) + (int(to_mon)-int(from_mon))*30
    return days 
    # print(days)

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
# # print(tot_amount)
# print("Customer Name:",tot_amount['Customer Name'])
# print("No of days:",tot_amount['No of days'])
# print("Total amount:",tot_amount['Total amount'])

def calculate_time(race_details):
    ans=[]
    for i in race_details:
        d={}
        arr = i.split(":")
        time = round(200/int(arr[2]),1)
        d["Id"] = arr[0]
        d["Name"] = arr[1]
        d["Time"] = time
        ans.append(d)
    # print(ans)
    return ans 

def find_qualifiers(race_details,time):
    ans = []
    for i in race_details:
        if(i["Time"] <= time):
            ans.append(i["Name"])
    return ans 


# n = int(input("Enter the no. of race participants:"))
# lst = []
# for i in range(n):
#     lst.append(input())
# details = calculate_time(lst)
# time_n = float(input("Enter the time to qualify for the next level:"))
# ans = find_qualifiers(details,time_n)
# if(len(ans)==0):
#     print("No one is qualified")
# else:
#     print("The qualified participants are:")
#     for i in ans:
#         print(i)

def create_list(factors):
    arr = factors.split(",")
    return arr

#A antigens, B antigens, anti-A antibodies, anti-B antibodies,

def deduce_blood_group(blood_details):
    arr = ["A","B","anti-A","anti-B"]
    ans=[]
    res = ""
    for i in range(len(blood_details)):
        if(blood_details[i] == "y"):
            ans.append(arr[i])
    type_1,type_2 = ans[0],ans[1]
    if((type_1 == "A" and type_2 == "anti-A") or (type_1=="B" and type_2 == "anti-B")):
        return False
    d={}
    d["A","B"] = "AB"
    d["A","anti-B"] = "A"
    d["B","anti-A"] = "B"
    d["anti-A","anti-B"] = "O"
    if(blood_details[-1] == "+"):
        res = d[type_1,type_2] + "+"
    else:
        res = d[type_1,type_2] + "-"
    return res


# st = input("Enter y/n for A antigens, y/n for B antigens, y/n for anti-A antibodies, y/n for anti-B antibodies, and +/- for Rh factor (as comma separated values):")
# vals = create_list(st)
# ans = deduce_blood_group(vals)
# if(ans == False):
#     print("Incorrect combination of antigens/antibodies entry")
# else:
#     print("Deduced blood group:",ans)

def create_player(player_id,player_name,matches_played,runs_scored):
    d={}
    d["Id"] = player_id
    d["Name"] = player_name
    d["Matches_Played"] = matches_played
    d["Runs_Scored"] = runs_scored
    return d 

def display_player(players_details):
    ans = []
    for i in players_details:
        if(i['Runs_Scored']>=100):
            ans.append(i)
    if(len(ans)>0):
            n=0
            for i in ans:
                print("\nPlayer ",n+1,":")
                print("Id:",i["Id"])
                print("Name:",i["Name"])
                print("Matches_Played:",i["Matches_Played"])
                print("Runs_Scored:",i['Runs_Scored'])
                n += 1
    else:
        print("\nNo player details found")

players = []
while(True):
    print("\n1. Create Player\n2. Display Player details\n3. Exit")
    choice = int(input("Enter the option:"))
    if(choice == 1):
        player_id = input("Player id:")
        player_name = input("Player name:")
        matches_played = int(input("Matches played:"))
        runs_scored = int(input("Runs scored:"))
        vals = create_player(player_id,player_name,matches_played,runs_scored)
        players.append(vals)
        # print(players)
    elif(choice == 2):
        display_player(players)
    else:
        print("Thank you")
        break


def find_each_round_winner(team1,team2):
    ans = []
    for i in range(len(team1)):
        if(team1[i] == team2[i]):
            ans.append("Equal")
        elif(team1[i] > team2[i]):
            ans.append("Team1")
        else:
            ans.append("Team2")
    return ans 

def count_winners(winner_list):
    d={'Team1':0,'Team2':0,'Equal':0}
    for i in winner_list:
            d[i] += 1
    return d 

# n = int(input("Enter the no of rounds:\n"))
# if(n>0):
#     team1,team2=[],[]
#     print("Enter the team1 points:")
#     for i in range(n):
#         team1.append(int(input()))
#     print("Enter the team2 points:")
#     for i in range(n):
#         team2.append(int(input()))
#     teams_list = find_each_round_winner(team1,team2)
#     vals = count_winners(teams_list)
#     # print(vals)
#     print(teams_list)
#     print("Team1:",vals["Team1"])
#     print("Team2:",vals["Team2"])
#     print("Equal:",vals["Equal"])
# else:
#     print("Invalid rounds")

def add_task(task,todo_list):
    todo_list.append(task)
    return todo_list

def mark_task_completed(index,todo_list):
    if(len(todo_list)>0):
        if(index > len(todo_list)-1):
            print("Invalid Input")
        else:
            todo_list.pop(index)
            for i in todo_list:
                print(i)
            return todo_list
    else:
        print("Invalid Input")
    return 


tasks = []
while(True):
    n = int(input("Enter a command (1 to add a task, 2 to mark a task complete, 3 to quit):"))
    if(n==1):
        task_name = input("Enter the task to add:")
        new_task_list = add_task(task_name,tasks)
        tasks = new_task_list
    elif(n==2):
        if(tasks):
            index = int(input("Enter the index of the task to mark as complete:"))
            updated = mark_task_completed(index,tasks)
            if(updated):
                tasks = updated 
        else:
            print("Invalid Input")
    elif(n==3):
        break 
    else:
        print("Invalid command")
        break


def create_record(children_records):
    ans=[]
    for i in children_records:
        d={}
        arr = i.split(":")
        weeks = int(arr[2])
        if(weeks>=1 and weeks<=24):
            d["Name"] = arr[0]
            d["Gender"] = arr[1]
            d["Weeks"] = arr[2]
            d["Contact"] = arr[3]
            ans.append(d)
    # print(ans)
    return ans 

def display_record(valid_records,weeks):
    c=0
    for i in valid_records:
        if(int(i["Weeks"]) <= weeks):
            c+=1 
            print("\nRecord ",c,":")
            print("Name:",i["Name"])
            print("Gender:",i["Gender"])
            print("Weeks:",i["Weeks"])
            print("Contact:",i["Contact"])

    if(c==0):
        print("No child under",weeks,"weeks has booked for the vaccination")
    elif(c==1):
        print("There is 1 child under",weeks,"weeks have booked for the vaccination")
    else:
        print("There are",c,"children under",weeks,"weeks who have booked for vaccination")


# n = int(input("Enter the no of children:\n"))
# print("Enter name, gender, weeks, and contact as colon-separated values:")
# arr=[]
# for i in range(n):
#     arr.append(input())
# records = create_record(arr)
# if(len(records)>0):
#     weeks = int(input("To display the records based on weeks since birth - Enter the no of weeks(<=24):"))
#     display_record(records,weeks)
# else:
#     print("No records available")


def check_availability(item,quantity,stock):
    if(item in stock and stock[item]>= quantity):
            return True 
    else:
        return False 
    
def place_order(item,quantity,stock,prices):
    tot_amt = 0 
    stock[item] = stock[item] - quantity
    tot_amt = prices[item]*quantity 
    print("Total amount:",tot_amt)
    print("Remaining stock details")
    for k,v in stock.items():
        print(k,":",v)




# item = input("Enter an item:")
# quantity = int(input("Enter a quantity:"))
# stock = {'Sports Balls':56,'Shin guards':50,'Gloves':60,'Footwear':15}
# prices = {'Sports Balls':100,'Shin guards':50,'Gloves':370,'Footwear':67}
# if(check_availability(item,quantity,stock)):
#     place_order(item,quantity,stock,prices)
# else:
#     print("Item is not available")


def compute_risk_score(patient_data):
    risk_factor = 0 
    age,gender,bp_level,cholestrol_level = int(patient_data[0]),patient_data[1],int(patient_data[2]),int(patient_data[3])
    if(age>60): risk_factor+=10
    else: risk_factor += 5

    if(gender == 'M'): risk_factor += 5 
    else: risk_factor += 3 

    if(bp_level>120): risk_factor += 10 
    else: risk_factor += 5 

    if(cholestrol_level>200): risk_factor+=15
    else: risk_factor += 10 

    return risk_factor

def predict_probability(risk_factor):
    return  round((1 - (1/(1+risk_factor))),2)


# patient_data = input("Enter the patient data\n").split(":")
# risk_factor = compute_risk_score(patient_data)
# prediction = predict_probability(risk_factor)
# print("The probability of the patient developing the disease is",prediction)

def validate_license_number(vehicle_details):
    license_number = vehicle_details.split(",")[2]
    if(re.match(r"AA99[199|200-202][9|0-2]\d+",license_number) and len(license_number)==15):
    # if(re.match(r"^AA99\d+$",license_number)):
        return True 
    else:
        return False 
    
def generate_parking_id(vehicle_details):
    vehicle_details = vehicle_details.split(",")
    Name = vehicle_details[1]
    license_number = vehicle_details[2]
    vehicle_type = vehicle_details[3]
    duration_in_hrs = int(vehicle_details[-1])
    parking_id = ""
    Amount = 0
    if(vehicle_type == "Two wheeler"):
        parking_id += 'A'
        Amount = 20
    else:
        parking_id += 'B'
        Amount = 30 
    # print(license_number[-8:])
    parking_id += str(sum([int(i) for i in license_number[-7::]]))
    parking_id += Name[0]
    d={}
    d["Name"],d["Parking Id"],d["Amount"] = Name,parking_id,round(float(duration_in_hrs*Amount),1)
    return d 

# vehicle_details = input("Enter the Details:\n")
# if(validate_license_number(vehicle_details)):
#     print(generate_parking_id(vehicle_details))
# else:
#     print("Invalid Input")

def is_ugly(number_list):
    # print(number_list)
    prime_factors = [2,3,5]
    flag = False
    ans=[]
    for i in number_list:
        factors = []
        primes = []
        for j in range(2,i):
            if(i%j == 0):
                factors.append(j)
        # print("Factors = ",factors)
        for k in factors:
            for q in range(2,k//2 + 1):
                if(k%q == 0):
                    break 
            else:
                primes.append(k)
        # print("Primes = ",primes)
        for p in primes:
            if p in prime_factors:
                flag = True 
            else:
                flag = False 
        if(flag):
            ans.append(i)
    if(len(ans)>0):
        for i in ans:
            print(i)
    else:
        print("No ugly numbers found")
        

# number_list = list(map(int,input("Enter the numbers (as comma-separated values):").split(",")))
# is_ugly(number_list)
# from sympy import *

# print(list(sieve.primerange(2,500)))
# print(list(primerange(2,500)))
# print(isprime(9))

def ugly_2(lst):
    flag = False
    prime_factors = [2,3,5]
    ans = []
    for i in lst:
        for j in range(2,i):
            if(i%j == 0 and isprime(j)):
                if j in prime_factors:
                    flag = True
                else:
                    flag = False 
        if(flag):
            ans.append(i)
    if(len(ans)>0):
        print(ans)
    else:
        print("No ugly numbers present")

# ugly_2([11,22,33,44,55])

def filter_regno(reg_no):
    # arr = [float(i) for i in reg_no]
    # print(reg_no)
    ans=[]
    for i in reg_no:
        if(i[:4] == "7119"):
            pass
        else:
            ans.append(i)
    return ans

# n = int(input("Enter the no. of students registered for the webinar:"))
# arr = []
# print("Enter the register numbers:")
# for i in range(n):
#     arr.append(input())
# ans = filter_regno(arr)
# print("Register numbers of students from other Universities:",end="")
# print(ans)


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
        # print(ans,list_1)
        if(len(ans)==0):
            return "All students have scholarships"
        else:
            return ans 

# string_1 = input()
# string_2 = input()
# val = check_scholarship(string_1,string_2)
# if(type(val)==list):
#     print("Students without scholarships:",end="")
#     print(*val,sep=",") 
# else:
#     print(val)
    
def calculate_score(score_values):
    c = 0
    avg = (sum(score_values)/len(score_values))/2
    if(score_values.count(0) == len(score_values)):
        return 0
    for i in score_values:
        if i >= avg:
            c+=1 
    return c 


# n = int(input("Enter the size of the score card:"))
# print("Enter the score values:")
# arr = []
# for i in range(n):
#     arr.append(float(input()))
# print("The score values that are equal to or above 50% of the average score:",calculate_score(arr)) 


def analyze_comments(input_string,keywords):
    strings = input_string.split("\n")
    # print(strings)
    ans=[]
    for i in strings:
        arr = i.split(":")
        for j in keywords:
            if j in arr[1]:
                ans.append(arr[1].lstrip())

    for i in ans:
        print(i)
 
# str = "user1: I love this post!\nuser2: This is a great post!\nuser3: I totally agree with user1\nuser4: This post is amazing!"
# keywords = ["love","great","amazing"]
# analyze_comments(str,keywords)


def calculate_amount(credict_points):
    cash_back = 0
    for i in credict_points:
        if(i>=50): cash_back += i*5
        elif(i>=30 and i<50): cash_back += i*2
        elif(i<30): cash_back += i*1
    if(cash_back<=0):
        cash_back = 0
    return cash_back

# n = int(input("Enter the no. of travel credit card users:"))
# users = []
# c=0
# for i in range(n):
#     users.append(int(input("Enter the credit points for user {} :\n".format(c+1))))
#     c+=1 
# print("Total cash-back amount:",calculate_amount(users))

def check_rating(rating_list):
    r_5,r_10 = [],[]
    for i in rating_list:
        if(i>=0 and i<=5):
            r_5.append(i)
        elif(i>=6 and i<=10):
            r_10.append(i)
        else:
            return "Invalid Rating"
    if(len(r_5) > len(r_10)):
        return "The highest rating is for 0-5"
    elif(len(r_10)>len(r_5)):
        return "The highest rating is for 6-10"
    else:
        return "Ratings are equal"

# n = 6
# arr = [3,2,5,6,8,9]
# print(check_rating(arr))

def find_winner(sales_rep1,sales_rep2):
    s1,s2=0,0
    for i in range(len(sales_rep1)):
        if(sales_rep1[i] > sales_rep2[i]):
            s1 += 1
        else:
            s2 += 1
    if(s1>s2):
        return "Sales Representative 1 is the winner"
    elif(s2>s1):
        return "Sales Representative 2 is the winner"
    else:
        return "Both are winners"

# n=5
# arr1=[45,67,89,20]
# arr2=[34,56,90,60]
# print(find_winner(arr1,arr2))



def find_average_temperature(input_string):
    arr = input_string.split(",")
    arr = [int(i) for i in arr]
    avg_tmp = round(sum(arr)/len(arr),2)
    return [avg_tmp,arr.index(max(arr))+1]

# arr = find_average_temperature("31,33,35,37,28,33,41,36")
# avg_temp,day = arr[0],arr[1]
# print(avg_temp,day)


def calculate_calories(input_string1_list,input_string2_list):
    calorie = 0
    if(input_string1_list[1] == 'sedentary'):
        calorie += 1.2 
    elif(input_string1_list[1] == 'moderately active'):
        calorie += 1.55
    else:
        calorie += 1.9 
    if(input_string1_list[0] == 'male'):
        calorie *= (((10*input_string2_list[2]) + (6.25*input_string2_list[1]) - (5*input_string2_list[0])) - 161 )
    else:
         calorie *= (((10*input_string2_list[2]) + (6.25*input_string2_list[1]) - (5*input_string2_list[0])) + 5 )
    return calorie 

g,al = 'female','sedentary'
a,h,w = 23,153,60 
print(calculate_calories([g,al],[a,h,w]))