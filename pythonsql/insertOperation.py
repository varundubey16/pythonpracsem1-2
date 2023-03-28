import mysql.connector as ms

connection = ms.connect(host="localhost", user="root",
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
connection.close()
