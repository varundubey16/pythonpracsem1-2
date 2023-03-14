#file handling in python

'''file=open("C:/Users/varun/Desktop/MS.txt", "a+")
file1=file.read()
print(file1)

my_file=open("C:/Users/varun/Desktop/cms.txt" ,"r")
x1=my_file.read()
print(x1)

my_file2=open("C:/Users/varun/Desktop/VARUN.txt" ,"w+")
my_file2.write(x1)
my_file2.seek(0)
print(my_file2.read())'''

'''my_file=open("C:/Users/varun/Desktop/Python File Handling/myfile1.txt" ,"r")
x1=my_file.read()
print(x1)
my_file=open("C:/Users/varun/Desktop/Python File Handling/myfile2.txt" ,"w+")
my_file.write(x1)
my_file.seek(0)
print(my_file.read())'''

my_file=open("C:/Users/varun/Desktop/Python File Handling/myfile1.txt" , "r")
print(my_file.read(8))

my_file2=open("C:/Users/varun/Desktop/Python File Handling/myfile2.txt")
my_file2.write("/nWelcome to I/O in Python.")
my_file2.seek(0)