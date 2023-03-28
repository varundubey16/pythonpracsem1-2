# creating and using a database

import mysql.connector as ms


'''connection = ms.connect(host="localhost", username="root", password="")
# creating a cursor
cursor = connection.cursor()
# executing queries
cursor.execute("CREATE DATABASE bca_base")
cursor.execute("USE bca_base")
# checking current database
cursor.execute("SELECT DATABASE()")
result = cursor.fetchone()
print(result[0])
cursor.close()
connection.close()'''


'''connection = ms.connect(host="localhost", user="root", password="", database="bca_base")
cursor = connection.cursor()
table_query = "CREATE TABLE emp(emp_id int(6), emp_name varchar(20), emp_add varchar(25), emp_phone int(10))"
cursor.execute(table_query)
# check tables
check_query = "SHOW TABLES"
cursor.execute(check_query)
results = cursor.fetchall()
for table in results:
    print(table)
connection.commit()
cursor.close()
connection.close()'''


'''emp_id = input("Enter employee id: ")
values = (emp_id, )

connection = ms.connect(host="localhost", user="root",
                        password="", database="bca_base")
cursor = connection.cursor()

select_query = 'DELETE from emp WHERE emp_id=(%s)'
cursor.execute(select_query, values)

# check updated records
check_query = "SELECT * FROM emp"
cursor.execute(check_query)
results = cursor.fetchall()

for rows in results:
    print(rows)

connection.commit()
cursor.close()
connection.close()'''


'''connection = ms.connect(host="localhost", user="root",
                        password="", database="bca_base")
cursor = connection.cursor()
emp_id = input("Enter id: ")
emp_name = input("Enter name: ")
emp_add = input("Enter address: ")
emp_phone = input("Enter phone number: ")
insert_query = "INSERT INTO emp(emp_id, emp_name, emp_add, emp_phone) VALUES (%s, %s, %s, %s)"
values = (emp_id, emp_name, emp_add, emp_phone)
cursor.execute(insert_query, values)
# check updated records
check_query = "SELECT * FROM emp"
cursor.execute(check_query)
results = cursor.fetchall()
for rows in results:
    print(rows)
connection.commit()
cursor.close()
connection.close()'''


'''connection = ms.connect(host="localhost", user="root",
                        password="", database="bca_base")
cursor = connection.cursor()
select_query = 'SELECT * FROM emp WHERE emp_add="Stazna Living, Gokhlaenagar, Pune"'
cursor.execute(select_query)
results = cursor.fetchall()
for rows in results:
    print(rows)
connection.commit()
cursor.close()
connection.close()'''

'''emp_id =input("Enter employee id: ")
new_phone = input("Enter new phone number: ")
values = (new_phone, emp_id)
connection = ms.connect(host="localhost", user="root",
                        password="", database="bca_base")
cursor = connection.cursor()
select_query = 'UPDATE emp SET emp_phone=(%s) WHERE emp_id=(%s)'
cursor.execute(select_query, values)
# check updated records
check_query = "SELECT * FROM emp"
cursor.execute(check_query)
results = cursor.fetchall()
for rows in results:
    print(rows)
connection.commit()
cursor.close()
connection.close()'''

'''import mysql.connector
db=mysql.connector.connect(host="localhost", user="root", password="",database="bca_base")
cursor=db.cursor()
cursor.execute("SHOW TABLES")
results=cursor.fetchall()
for table_name in results:
   print(table_name)'''

import mysql.connector
db=mysql.connector.connect(host="localhost", user="root", password="",database="bca_base")
cursor=db.cursor()
cursor.execute("select * from emp")
results=cursor.fetchall()
for table_name in results:
   print(table_name)