# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Amir#rt33",
#     database="mydatabase"
# )
# mycursor=mydb.cursor()
# mycursor.execute("SELECT COUNT(address) FROM customers")
# result = mycursor.fetchall()
# print(result[0][0])

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
# mycursor.execute("SELECT * FROM customers ORDER BY name DESC ")
# result=mycursor.fetchall()
# for i in result:
#     print(i)

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Amir#rt33",
    database="mydatabase"
)
mycursor=mydb.cursor()

sql="DELETE FROM customers WHERE name = %s"
val=[("Amy",),("Ben",),("chuck",)]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount)