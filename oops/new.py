# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
'''
class Employee:
    def message(self):
        print('This message is from Employee Class')
  
class Department(Employee):
  
    def message(self):
        print('This Department class is inherited from Employee')
  
emp = Employee()
emp.message()
  
print('------------')
dept = Department()
dept.message()

'''










#composit/container 
class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay)
        
             
      
    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() + self.bonus)
 
#component
class Salary:
    def __init__(self, pay):
        self.pay = pay
    def get_total(self):
        return (self.pay*12)
 
 
obj_emp = Employee(300, 500)
print(obj_emp.annual_salary())






'''














#SINGLE INHERITANCE---> MULTILEVEL
class GrandParent:
    def run(self):
        print("Grandparent method")

class Parent(GrandParent):
    def show(self):
        print("parent method")
        
class Child(Parent):
    def display(self):
        print("child method")
        
        
c = Child()
c.display()
c.show()
c.run()


#p = Parent()
#p.display()
    
class Parent:
    def __init__(self,name):
        self.name=name
    def show(self):
        return self.name
        
class Child(Parent):
    def __init__(self,name,age):
        Parent.__init__(self,name)
        self.age=age
    def display(self):
        return "%s is %s year old. " % (self.name,self.age)
     
          
        
c = Child('John',24)
print(c.display())
print(c.show())





#Hierarchical inheritance with method overriding

class Person():
    def __init__(self, name):
        self.name = name
    def get_details(self):
        return self.name

class Student(Person):
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
    def get_details(self):
        return "%s studies %s and is in %s year." % (self.name, self.branch, self.year)

class Teacher(Person):
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers
    def get_details(self):
        return "%s teaches %s" % (self.name, ','.join(self.papers))
        
person1 = Person('John')
student1 = Student('vishal','Computer', 2003)
teacher1 = Teacher('Ram', ['Java', 'Python'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())

#Multiple inheritance
class Math:  
    def math_marks(self,a):  
        return a;  
    
class Science:  
    def sci_marks(self,b):  
        return b;  
class TotalMarks(Math,Science):  
    def final_mark(self,a,b):  
        return a+b;  
d = TotalMarks()  
print(d.math_marks(70))  
#print(d.sci_marks(90))  
#print(d.final_mark(70,90)) 


#method overloading
class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print("Area of Rectangle:",(a*b))
        elif a!=None:
            print("Area of square:",(a*a))
        else:
            print("Nothing to find")
    def product(self,a, b):
        p = a * b
        print(p)
    def product(self, a, b, c):
        p = a * b * c
        print(p)
       

obj1=Area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)
#obj1.product(2,3)
obj1.product(2,3,4)



 





class Example:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def add(self):
        return self.x + self.y
        
e = Example(8, 6)  #object initialization
e1 = Example(6, 7)  #object initialization
e2 = Example(8, 6)  #object initializationv
e3 = Example(9, 6)  #object initialization
e4 = Example(11, 6)  #object initialization
print(e1.add())
print(e2.add())
print(e3.add())
print(e4.add())







class Student():   
    
    def __init__(self, name, branch, year):
        self.name = name 
        self.branch = branch
        self.year = year     #instance var
        print("A student object is created.")
    def print_details(self):
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)


std1 = Student('Vishal','Computer','2003')
std1.print_details()


























#write a python program to read file ,display the content of it.. 

my_file1 = open("F:/MyPython/test.txt", "r")
x1=my_file1.read()
print(x1)

''




#write a python program to read file ,display the content of it.. 
#Create a new file and write the content of old file to new file and 
#display the content of the same.

my_file1 = open("F:/MyPython/test.txt", "r")
x1=my_file1.read()

my_file2 = open("New_file20MARCH.txt", "w+")
my_file2.write(x1)
my_file2.seek(0)
print(my_file2.read())






#open and read a file and read
my_file = open("F:/MyPython/test.txt", "r")
print(my_file.read())


#create  and write into a file
my_file2 = open("thursday.txt", "w+")
my_file2.write("Today is Thursday")
my_file2.seek(0) #bring to beginning
x=my_file2.read()
print(x)


#append
my_file2 = open("thursday.txt", "a+")
my_file2.write("\nWelcome to File handling in Python")
my_file2.seek(0) #bring to beginning
x=my_file2.read()
print(x)


#seek
# Second parameter is by default 0 
# sets Reference point to tenth  
# index position from the beginning 
my_file = open("F:/MyPython/test.txt", "r")
x=my_file.read()
print(x)
my_file.seek(10)
# prints current postion 
print(my_file.tell()) 
print(my_file.readline())  
my_file.close() 


#reading content in file

my_file = open("D:/MyPython/test.txt", "r")
content=my_file.read()
print(content)
my_file.close()


#reading content line by line
my_file = open("test.txt", "r")
content1=my_file.readlines()
for x in content1:
   print(x)
my_file.close()





























a = 3
b = 0
c = a/b
print('Hi there')




a = 3
b = 0
try:
    c=a/b
except ZeroDivisionError:
    print('Calculation error , zero value in denominator')
    
print('Hi there')


try:
    a =eval(input('Enter a number: '))
    print (3/a)
    #raise NameError
    #raise ZeroDivisionError
except NameError: 
   print('Please enter a number bet 1-9.')
except ZeroDivisionError:
    print('Can not enter 0.')


x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")




try:
    a=4
    c=a/0
except Exception as e: 
    print(e)
    
try:
    a =eval(input('Enter a number: '))
    c = 3/a 
except Exception as e:
    print(e)
else:
   a=a+5
   print(a)

print('continue')
   
   

try:
    a =eval(input('Enter a number: '))
    print(3/a)
except NameError:
   print('Please enter a number bet 1-9.')
except ZeroDivisionError:
    print('Can not enter 0.')
else:
   a=a+5
   print(a)
finally:  
     print('This block always executes')
   


try:
    file = open('test31.txt', 'r')
except IOError:
    print('File not exists')
else:
    s = file.read()
    print(s)
finally:
    print('This block always executes')
    #file.close()



'''














'''
mydict = {
  "brand": "Ford",
  "model": "Figo",
  "year": 2000,
  "color":["red","blue"]
}
print(mydict)
print(mydict["brand"])

mydict1 = {
  "brand": "Ford",
  "model": "Figo",
  "year": 2000,
  "year": 2001
  }

print(mydict1)
print(len(mydict))
print(len(mydict1))

#update dist
mydict1["brand"]="Maruti"
print(mydict1)

#add new entry
mydict1["price"]="8L"
print(mydict1)

#delete entry
del mydict1["year"]  #1way using del function
print(mydict1)





Dict = {1: 'JavaTpoint', 2: 'Peter', 3: 'Thomas'}   
pop_ele = Dict.pop(3)   #2nd way using pop function
print(Dict)
Dict.popitem()   
print(Dict)
Dict.clear()  
print(Dict)

#print all keys
Employee = {"Name": "John", 
            "Age": 29, 
            "salary":25000,
            "Company":"GOOGLE"}    

for x in Employee:    
    print(x)  
print("\n")

#print all values
   
for x in Employee:    
    print(Employee[x]) 
print("\n")
#value() to print values
for x in Employee.values():    
    print(x)  
#item method to print all in dictionary
print("\n")
for x in Employee.items():    
    print(x) 

city = input("What part of Maharashtra did you visit? ")
answer = f"Great, {city} is an interesting city!"
print(answer)
'''






















'''
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#allow duplicate
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#one item
thistuple = ("apple","ff")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male",100,"pqr")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1[0])
print(tuple1[-1])
print(tuple1[1::2])
print(tuple1[1:4:2]) #start:end:step+
print(tuple1[0::2]) #start:end:step+

print(tuple1[2::1])
print(tuple1[::-1])


tuplex = ("PYTHON.MYKVS.IN", True,100, 1.0)
print(tuplex)
a=tuplex[3]
print(type(a))



#len function
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#min max

tuple4=('maths', 'che', 'phy', 'bio')
tuple5=(456, 700, 200)
print ("Max value element : ", max(tuple4))
print ("Max value element : ", max(tuple5))

print ("min value element : ", min(tuple4))
print ("min value element : ", min(tuple5))

#tuple

aList = [123, 'xyz', 'zara', 'abc']
aTuple = tuple(aList)
print("Tuple elements : ", aTuple)

print((1, 2, 3) + (4, 5, 6))
print(('Hi!',) * 4)
print(3 in (1, 2, 3))
for x in (1, 2, 3): print(x)

#adding element into tuple
print(type(tuple4))
#tuple4[4]='eng'
y=list(tuple4)
print(type(y))
print(y)
y.append('eng')
print(y)
tuple4=tuple(y)
print(tuple4)




tuple4=('maths', 'che', 'phy', 'bio')

del tuple4
print("tuple4 deleted")

'''



'''

groceries=[]
groceries=["milk",'bread','eggs']
print(groceries) # all the elements
print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[:2])
groceries[0]='cheese'
print(groceries)

mylist=[1,'2',3.0,False]
print(mylist)

mylist1=[5,
         2,
         1,
         [0.2,0.3,"a",[11,22,33]],["aa","bb",11],
         6,7]
         
print(mylist1)
print(mylist1[0])
print(mylist1[1])
print(mylist1[3]) #[0.2,0.3,"a"]
print(mylist1[4])
print(mylist1[4][1])  #bb
print(mylist1[3][2])  #a
print(mylist1[3][3][1])  #22


sliced_List = mylist1[2:4] 
print("\nSlicing elements in a range 2-4: ") 
print(sliced_List) 

#len function
len_mylist1=len(mylist1)
print(len_mylist1)
print(mylist1[4-len_mylist1][1]) #bb

mylist1.remove(2)# remove given value
print(mylist1)
mylist1.pop() #removes last element
print(mylist1)
mylist1.pop(2) #remove element at given index
print(mylist1)
mylist1.insert(1,22)
print(mylist1)







mylist2=[5,3,7,2,8,9,1]
mylist2.sort()
print(mylist2)
mylist2.sort(reverse=True)
print(mylist2)
mylist2.append(4)
print(mylist2)
print("maximum:",max(mylist2))
print("minimum:",min(mylist2))
print("sum=:",sum(mylist2))

#extend
l1=[70,20]
l2=[30,10]
print(l1+l2)
l1.extend(l2)
print(l1)

print(sorted(l1))
print(l1)
l1.sort()
print(l1)















#Python Sequence Operations
#1.Concatenation
print("Ayu"+"shi")
#2.Integer Multiplication
print('ba'+'na'*2);
#3.Membership
print('men' in 'Disappointment')
#4.Python Slice
print('Ayushi'[1:4])
'''
























