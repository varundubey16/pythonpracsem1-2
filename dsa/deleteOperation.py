import mysql.connector as ms

emp_id = input("Enter employee id: ")
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
connection.close()
