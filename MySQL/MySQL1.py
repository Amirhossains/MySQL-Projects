# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Amir#rt33",
#     database="mydatabase"
# )
# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE TABLE ferer (name VARCHAR(10) NOT NULL ,age INT)")

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Amir#rt33",
    database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT version()")
result = mycursor.fetchone()
print(result)