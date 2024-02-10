# import mysql.connector
#
# try:
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Amir#rt33",
#         database="mydatabase"
#     )
#     mycursor=mydb.cursor()
#     val=[]
#     b = []
#     mycursor.execute("SELECT * FROM people WHERE age=19")
#     result1 = mycursor.fetchall()
#     sql = ("UPDATE people SET age=18 WHERE name=%s ")
#     for i in result1:
#         if i[0]!='sadra' :
#             continue
#         b.append(i[0])
#     for i in b:
#         a = []
#         a.append(i)
#         a = tuple(a)
#         val.append(a)
#
#     mycursor.executemany(sql,val)
#
#     mydb.commit()
# except ConnectionError as error:
#     print("you didnt connect to the server, \nsome things went wrong.")
# else :
#     mycursor.close()
#     print("your job is seccessfully done! \nour connection closed!")

# # (===========================================================================)

def ageIncreasing():
    try:
        import mysql.connector

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Amir#rt33",
            database="mydatabase"
        )
        val=[]
        mycursor = mydb.cursor()
        sql = (f"UPDATE people SET age=%s WHERE name=%s")
        mycursor.execute("SELECT * FROM people")
        result = mycursor.fetchall()
        for i in result:
            b = []
            b.append(i[1]+1)
            b.append(i[0])
            b = tuple(b)
            val.append(b)

        mycursor.executemany(sql,val)
        mydb.commit()
    except mysql.connector.Error as error:
        print("you did not connect to the server :( \nsomethings went wrong.",format(error))
    else:
        if  mydb.is_connected():
            mydb.close()
            print("The age of all the members was increased by one year. \nMySQL connection is closed.")
# ageIncreasing()
# After a successful MySQL connection, we set auto-commit to False, i.e.,
# we need to commit the transaction only when both the transactions complete successfully