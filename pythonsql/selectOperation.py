import mysql.connector as ms

connection = ms.connect(host="localhost", user="root",
                        password="", database="bca_base")
cursor = connection.cursor()

select_query = 'SELECT * FROM emp WHERE emp_add="Mumbai"'
cursor.execute(select_query)

results = cursor.fetchall()

for rows in results:
    print(rows)

connection.commit()
cursor.close()
connection.close()
