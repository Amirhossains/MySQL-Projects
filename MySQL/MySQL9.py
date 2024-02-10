import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Amir#rt33",
    database="mydatabase"
)
mycursor = mydb.cursor()

sql = "SELECT \
      Students.name AS student, \
      Teachers.name AS favorite \
      FROM Students \
      INNER JOIN Teachers ON Students.fav = Teachers.id"
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)

# # (============================================================================================)

# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Amir#rt33",
#     database="mydatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE hospital (Hospital_Id INT NOT NULL , Hospital_Name TEXT NOT NULL , Bed_Count INT NOT NULL)")
# mycursor.execute("CREATE TABLE Doctor (Doctor_Id INT NOT NULL , Doctor_Name TEXT NOT NULL , Hospital_Id INT NOT NULL , Joining_Data TEXT NOT NULL , Speciality TEXT NULL , Salary INT NULL , Experience INT NULL , PRIMARY KEY (Doctor_Id))")
# mydb.commit()

