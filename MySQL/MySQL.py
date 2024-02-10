# import mysql.connector
#
# mydb = mysql.connector.connect(
#     user="root",
#     host="localhost",
#     password="Amir#rt33",
#     database="mydatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute('SHOW DATABASES')
# for i in mycursor:
#     print(i)

import mysql.connector

mydb = mysql.connector.connect(
    user="root",
    host="localhost",
    password="Amir#rt33",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = ("INSERT INTO customers (name , address) VALUES (%s,%s)")
val = ("parhamzg","daneshgah")
mycursor.execute(sql,val)
mydb.commit()
mycursor.close()