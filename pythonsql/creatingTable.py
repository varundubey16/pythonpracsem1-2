import mysql.connector as ms

connection = ms.connect(host="localhost", user="root", password="", database="bca_base")
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
connection.close()