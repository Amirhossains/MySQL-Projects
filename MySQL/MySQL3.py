import mysql.connector

mydb = mysql.connector.connect(
    user="root",
    password="Amir#rt33",
    host="localhost",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
mycursor.close()

# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Amir#rt33",
#     database="mydatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT name FROM customers")
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
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchone()
# print(myresult)