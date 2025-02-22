
def ans(lst):
    d={}
    ans=[]
    for i in lst:
        ans.append(i[0])
    # lst.sort()
    for i in range(len(lst)):
        for j in range(len(lst)):
            if(lst[i][0] == ans[j]):
                if lst[i][0] not in d:
                    d[ans[j]] = lst[i]
                elif(d[ans[j]] != lst[i][0]):
                    d[ans[j]] += ","+lst[i]
                    print(d[ans[j]])
    print(d)
    return ans

from collections import Counter 
def res(lst):
    rep = []
    for i in lst:
        rep.append(i[0])
    rep.sort()
    ans = Counter(rep)
    res = {}
    for k,v in ans.items():
        res[k] = v
    return res

# lst = ["Aman","Bhavan","Chinmay","Ravi","Teja","Ananth","Bhuvan","Firoz"]
# # print(ans(lst))
# print(res(lst))

'''
You are provided with a class Contact with the following attributes as private.
 
String firstName
 
String lastName
 
long  phoneNumber
 
String emailId
 
A 4 argument constructor and appropriate setters and getters to store and retrieve the details are also provided.
 
Create a class PhoneBook with attribute
 
List<Contact> phoneBook = new ArrayList<Contact>();
 
Write the getters and setters.
 
Write the following methods in the PhoneBook class.
 
public void addContact(Contact contactObj) - This method should add the contact object to the phoneBook list.
 
public List<Contact> viewAllContacts() - This method should return the list of all contacts available.
 
public Contact viewContactGivenPhone(long phoneNumber) -  This method should return the contact details which has the phoneNumber given as parameter.
 
public boolean removeContact(long phoneNumber) -  This method should remove the contact details which has the phoneNumber given as parameter.  
If removed return true.  Else if the phone number is not available return false.
 
Write a class Main with the main method.  Create the menu as shown in the Sample Input and Output and invoke the corresponding methods as per the choice provided.
'''
#Aggregation -> has a relationship

class Contact:
    def __init__(self,firstName,lastName,phoneNumber,emailId):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.emailId = emailId
        return 
    
class PhoneBook:
    def __init__(self):
        self.contacts = []

    def addContact(self,contact):
        self.contacts.append(contact)
    
    def viewAllContacts(self):
        return self.contacts

    def viewContactGivenPhone(self, phoneNumber):
        for i in self.contacts:
            if(phoneNumber == i.phoneNumber):
                return i
        raise Exception("Phone number not found")
    
    def removeContact(self,phoneNumber):
        for i in self.contacts: 
            if(phoneNumber == i.phoneNumber):
                self.contacts.remove(i)
                return True
        raise Exception("Phone number is not given")
    

# p1 = PhoneBook()
# p2 = PhoneBook()
# p1.addContact(Contact("Ravi","Teja","8106419630","krtp@gmail.com"))
# p2.addContact(Contact("Phani","Kumar","9502118729","sandy@infosys.com"))
# val1 = p1.viewAllContacts()
# val2 = p2.viewAllContacts()
# for i in val1:
#     print("First Contact : ",i.firstName,i.lastName,i.phoneNumber,i.emailId)      
# for i in val2:
#     print("second Contact : ",i.firstName,i.lastName,i.phoneNumber,i.emailId)      

# try:
#     i = p2.viewContactGivenPhone("9502118729")
#     print("Contact Details: ",i.firstName,i.lastName,i.phoneNumber,i.emailId)      
# except Exception as e:
#     print(e)


