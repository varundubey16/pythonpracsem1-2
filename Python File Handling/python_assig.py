#file handling in python

file=open("C:/Users/varun/Desktop/MS.txt", "a+")
file1=file.read()
print(file1)

my_file=open("C:/Users/varun/Desktop/cms.txt" ,"r")
x1=my_file.read()
print(x1)

my_file2=open("C:/Users/varun/Desktop/VARUN.txt" ,"w+")
my_file2.write(x1)
my_file2.seek(0)
print(my_file2.read())

my_file=open("C:/Users/varun/Desktop/Python File Handling/myfile1.txt" ,"r")
x1=my_file.read()
print(x1)
my_file=open("C:/Users/varun/Desktop/Python File Handling/myfile2.txt" ,"w+")
my_file.write(x1)
my_file.seek(0)
print(my_file.read())

my_file=open("C:/Users/varun/Desktop/Python File Handling/myfile1.txt" , "r")
print(my_file.read(8))

my_file2=open("C:/Users/varun/Desktop/Python File Handling/myfile2.txt")
my_file2.write("/nWelcome to I/O in Python.")
my_file2.seek(0)


# msteams i/o assignment
'''with open("python.txt", "w") as f:
    f.write("PRN,Name,DS Marks,Python Marks,Network Marks\n")
    f.write("1,Varun Dubey,80,85,90\n")
    f.write("2,Utsav Gupta,70,80,85\n")
    f.write("3,Nikhil Kumar,90,85,95\n")
    f.write("4,Jane Doe,85,90,80\n")
    f.write("5, John Doe,,75,80,75\n")'''
