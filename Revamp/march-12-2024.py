def makeString(s):
    digit = [s[p] for p in range(len(s)) if p%2 != 0]
    cnt = [s[q] for q in range(len(s)) if q%2 == 0]
    # print(i,j)
    st = ""
    for a in range(len(digit)):
        st += digit[a]*int(cnt[a])
    print(st)

def makeString(s):
    st=""
    for i in range(0,len(s),2):
        st += int(s[i])*s[i+1]
    print(st)

s = "2A3E7F"
makeString(s)

from collections import Counter
def   removeSpace(st):
    return st.replace(" ","")
 
def   removeDuplicates(st):
    d = Counter(removeSpace(st))
    s=""
    for k,v in d.items():
        s += k 
    return s 

def removeDuplicates(st):
    s=""
    for i in removeSpace(st):
        if i not in s:  
            s+=i 
    return s 

print("Removing spaces : ",removeSpace("Ravi teja Karavadi"))
print("Removing Duplicates : ",removeDuplicates("Ravi Karavadi Ravi teja"))

def  isPalindrome(st):
    if(st == st[::-1]):
        return True 
    else:
        return False
 
def  countPalindrome(listWords):
    c=0
    for i in listWords:
        if(isPalindrome(i)):
            c+=1 
    if(c>0):
        print("Palindromes : ",c)
    else:
        print("No palindrome found")

countPalindrome(["mom","Ravi","dad"])

from math import *

sums = int(input())
prods = int(input())
a,b,c=1,-sums,prods
# -b(+-)sqrt(b**2 - 4*a*c)/2*a
root =  int((-b-sqrt(b**2 - 4*a*c))/2*a)

print("Roots are : ",root,sums-root)