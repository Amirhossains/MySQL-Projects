# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Amir#rt33",
#     database="mydatabase"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("SELECT * FROM customers WHERE address = 'mollasadra'")
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)

# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Amir#rt33",
#     database="mydatabase"
# )
# mycursor = mydb.cursor()
# a = "SELECT * FROM customers WHERE address LIKE '%way%'"
# mycursor.execute(a)
# result = mycursor.fetchall()
# for i in result:
#     print(i)

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Amir#rt33",
    database="mydatabase"
)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE name = %s"
val = ("amir",)
mycursor.execute(sql,val)
result = mycursor.fetchall()
for i in result:
    print(i)