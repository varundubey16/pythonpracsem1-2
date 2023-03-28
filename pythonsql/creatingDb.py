# creating and using a database
import mysql.connector as ms

connection = ms.connect(host="localhost", username="root", password="")

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
connection.close()
