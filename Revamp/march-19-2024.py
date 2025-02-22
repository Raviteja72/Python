'''
Python Operator Overloading
===================
 
In Python, we can change the way operators work for user-defined types.
 
For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.
 
This feature in Python that allows the same operator to have different meaning according to the context is called operator overloading.
 
 
Advantages of Operator Overloading
Here are some advantages of operator overloading,
 
1. Improves code readability by allowing the use of familiar operators.
2. Ensures that objects of a class behave consistently with built-in types and other user-defined types.
3. Makes it simpler to write code, especially for complex data types.
4. Allows for code reuse by implementing one operator method and using it for other operators.
 
 
=====To overload the + operator, we will need to implement __add__() function in the class.
 
With great power comes great responsibility. We can do whatever we like inside this function. But it is more sensible to return the Point object of the coordinate sum.
 
 
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
 
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
 
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
 
 
p1 = Point(1, 2)
p2 = Point(2, 3)
 
print(p1+p2)  // p1.+(p2);
 
# Output: (3,5)
 
 
Similarly, we can overload other operators as well. The special function that we need to implement is tabulated below.
 
Operator	Expression	Internally
Addition	p1 + p2		p1.__add__(p2)
Subtraction	p1 - p2		p1.__sub__(p2)
Multiplication	p1 * p2		p1.__mul__(p2)
Power		p1 ** p2	p1.__pow__(p2)
Division	p1 / p2		p1.__truediv__(p2)
Floor Division	p1 // p2	p1.__floordiv__(p2)
Remainder (modulo)	
		p1 % p2		p1.__mod__(p2)
Bitwise Left Shift	
		p1 << p2	p1.__lshift__(p2)
Bitwise Right Shift	
		p1 >> p2	p1.__rshift__(p2)
Bitwise AND	p1 & p2		p1.__and__(p2)
Bitwise OR	p1 | p2		p1.__or__(p2)
Bitwise XOR	p1 ^ p2		p1.__xor__(p2)
Bitwise NOT	~p1		p1.__invert__()
 
 
Overloading Comparison Operators
Python does not limit operator overloading to arithmetic operators only. We can overload comparison operators as well.
 
Here's an example of how we can overload the < operator to compare two objects the Person class based on their age:
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # overload < operator
    def __lt__(self, other):
        return self.age < other.age
 
p1 = Person("Alice", 20)
p2 = Person("Bob", 30)
 
print(p1 < p2)  # prints True
print(p2 < p1)  # prints False
 
 
 
Similarly, the special functions that we need to implement, to overload other comparison operators are tabulated below.
 
Operator			Expression	Internally
Less than			p1 < p2		p1.__lt__(p2)
Less than or equal to		p1 <= p2	p1.__le__(p2)
Equal to			p1 == p2	p1.__eq__(p2)
Not equal to			p1 != p2	p1.__ne__(p2)
Greater than			p1 > p2		p1.__gt__(p2)
Greater than or equal to	p1 >= p2	p1.__ge__(p2)
'''

class Person:
    def __init__(self,name ,age,address):
        self.name = name 
        self.age = age 
        self.address = address 

    def __str__(self):
        return "Name : {0}\nAge : {1}\nAddress : {2}".format(self.name,self.age,self.address)
    
    def __gt__(self,other):
        if(self.age > other.age):
            return Person(self.name,self.age,self.address)
        elif(self.age == other.age):
            if(self.address < other.address):
                return Person(self.name,self.age,self.address)
            else:
                return Person(other.name,other.age,other.address)
        else:
            return Person(other.name,other.age,other.address)

# p1 = Person("Ravi",22,"Dpl")
# p2 = Person("Phani",22,"Ban")
# print(p1>p2)

class myList:
    def __init__(self,lst):
        self.lst = lst 

    def __str__(self):
        return "My list : {}".format(self.lst)

    def __sub__(self,other):
        new_lst = []
        for i in range(len(self.lst)):
            # print(self.lst[i])
            if self.lst[i] not in other.lst:
                new_lst.append(self.lst[i])
        # print(new_lst)
        return myList(new_lst)

# m1 = myList([10,20])
# m2 = myList([10,20,70,80])
# try:
#     val = m1 - m2 
#     if(len(val) > 0):
#         print(val)
#     else:
#         raise Exception 
# except:
#     print("First list have no common element")
    

class complex:
    def __init__(self,real,imaginary):
        self.real = real 
        self.imaginary = imaginary 
    def __str__(self):
        return "{0}{1}".format(self.real,self.imaginary)
    def __add__(self,other):
        return complex(self.real+other.real, self.imaginary+other.imaginary)
    def __sub__(self,other):
        return complex(self.real-other.real,self.imaginary-other.imaginary)
    def __mul__(self,other):
        return complex(self.real*other.real,self.imaginary*other.imaginary)

# c1 = complex(1,3)
# c2 = complex(2,5)
# print(c1+c2)
# print(c1-c2)
# print(c1*c2)

class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
 
    def __str__(self):
        return "{0},{1}".format(self.real,self.imaginary)
   
    def __add__(self,other):
        self.real=self.real+other.real
        self.imaginary=str(int(self.imaginary[0:-1])+int(other.imaginary[0:-1]))+"i"
        return Complex(self.real,self.imaginary)
    def __sub__(self,other):
        self.real=self.real - other.real
        # print(self.real)
        self.imaginary=str(int(self.imaginary[0:-1]) - int(other.imaginary[0:-1]))+"i"
        return Complex(self.real,self.imaginary)
    def __mul__(self,other):
        self.real=self.real*other.real
        self.imaginary=str(int(self.imaginary[0:-1])*int(other.imaginary[0:-1]))+"i"
        return Complex(self.real,self.imaginary)
 
x1=Complex(12,"15i")
x2=Complex(3,"6i")
# print("Add : ",x1+x2)
print("Sub : ",x1-x2)
# x5=x1*x2
print("Mul : ",x1*x2)



