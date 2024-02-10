# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Amir#rt33",
#     database="mydatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("DROP TABLE IF EXISTS fuck")

# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Amir#rt33",
#     database="mydatabase"
# )
# mycursor= mydb.cursor()
#
# mycursor.execute("UPDATE people SET name='parhamzg' WHERE name='parham'")
# mydb.commit()

import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Amir#rt33",
    database="mydatabase"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM people LIMIT 2 OFFSET 1")
result = mycursor.fetchall()
for I in result:
    print(I)