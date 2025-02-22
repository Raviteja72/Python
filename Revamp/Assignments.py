class Book:
    def __init__(self,isbnno,bookName,author):
        self.isbnno = isbnno
        self.bookName = bookName
        self.author = author 
    
class Library:
    def __init__(self):
        self.bookList = []
    
    def addBook(self,book):
        self.bookList.append(book)
        # print(self.bookList)
    
    def isEmpty(self):
        if(len(self.bookList) == 0):
            return True 
        else:
            return False 
    
    def viewAllBooks(self):
        return self.bookList
    
    def viewBooksByAuthor(self,author):
        ans = []
        for i in self.bookList:
            if(i.author == author):
                ans.append(i)
        if(len(ans)>0):
            return ans 
        else:
            raise Exception("The list is empty no author present")
    
    def countnoofbook(self,bookName):
        c = 0 
        for i in self.bookList:
            if(i.bookName == bookName):
                c += 1 
        if(c>0):
            return c 
        else:
            raise Exception("No books present")

# l = Library()
# while(True):
#     print("1.Add Book\n2.Display all book details\n3.Search Book by author \n4.Count number of books - by book name\n5.Exit")
#     choice = int(input("Enter your choice:\n"))
#     try:
#         if(choice == 1):
#             book_no = int(input("Enter the book no: "))
#             book_name = input("Enter the book name: ")
#             book_author = input("Enter the book author: ")
#             l.addBook(Book(book_no,book_name,book_author))
#         elif(choice == 2):
#             lst = l.viewAllBooks()
#             print()
#             for i in lst:
#                 print("Book Details : ",i.isbnno,i.bookName,i.author)
#         elif(choice == 3):
#             author_name = input("Enter the author name: ")
#             lst = l.viewBooksByAuthor(author_name)
#             print()
#             for i in lst:
#                 print("Book Details : ",i.isbnno,i.bookName,i.author)
#         elif(choice == 4):
#             name = input("Enter book name: ")
#             print("No. of books : ",l.countnoofbook(name))
#         else:
#             break
#     except Exception as e:
#         print(e)

#Assgn-1

# st = input()
# arr = st.split(":")
# adults = int(arr[1])
# if(adults >= 0):
#     children = int(arr[2])
#     if(children >= 0):
#         days = int(arr[3])
#         if(days > 0):
#             print(arr[0],"your booking is confirmed and the total cost is Rs",(adults*1000 + children*650)*days)
#         else:
#             print("Invalid input for number of days")
#     else:
#         print("Invalid input for number of children")
# else:
#     print("Invalid input for number of adults")

#Assign-2

n = int(input("Enter the number of teams\n"))
if(n<=1):
    print("Invalid input")
else:
    print("Enter the details")
    flag = True
    ans = {}
    maxy = []
    c=0
    for i in range(n):
        arr = input().split(":")
        # print(arr)
        first,second,third,fourth=float(arr[1]),float(arr[2]),float(arr[3]),float(arr[4])
        if(first>=1 and second>=1 and third>=1 and fourth>=1):
            tot_time = first+second+third+fourth
            maxy.append(tot_time)
        else:
            flag = False 
            break 
        ans[arr[0]] = tot_time
    # print(ans)
    if(flag):
        for k,v in ans.items():
            if(v == min(maxy)):
                print(k,"team wins the race in",v,"minutes")
                break
    else:
        print("Invalid number")


# import re 

# st = input("Enter the sentence\n")
# ans = ""
# if(re.match(r"^[a-z ]+$",st)):
#     arr = st.split(" ")
#     for i in range(len(arr)):
#         ans += ''.join(sorted(arr[i]))
#         if(i != len(arr)-1):
#             ans += " "
#     print(ans)
# else:
#     print(st,"is an invalid input")


class ManagementUtility:
    def __init__(self):
        self.playerStream = []
    
    def addPlayerscore(self,playerName,score):
        d = {}
        d[playerName] = score 
        self.playerStream.append(d)
        return self.playerStream
    
    def maximumScore(self):
        maxy = -1
        if(len(self.playerStream) > 0):
            for i in self.playerStream:
                for k,v in i.items():
                    if(v > maxy):
                        maxy = v 
            print("The maximum score of an individual player for these match is",maxy)
        else:
            print("No players found")

# m = ManagementUtility()
# while(True):
#     option = int(input("\n1. Add player score\n2. Display\n3. Exit\n"))
    
#     if(option == 1):
#         name = input("\nEnter the player name\n")
#         score = int(input("Enter the score\n"))
#         m.addPlayerscore(name,score)
#     elif(option == 2):
#         m.maximumScore()
#     else:
#         print("Thank you for using the application")
#         break 





