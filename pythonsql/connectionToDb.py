# establishing a connection
import mysql.connector as ms

connection = ms.connect(host="localhost", user="root",
                        password="", database="database_name")

if (connection.is_connected()):
    print("Connection established.")
else:
    print("Error.")

# dont forget to close the connection
connection.close()
