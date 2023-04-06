import mysql.connector as ms

emp_id =input("Enter employee id: ")
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
connection.close()
