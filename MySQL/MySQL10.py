from mysql.connector import Error
import mysql.connector
def mysqlConnection():
    print("You are connecting to the mysql database... \n ")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Amir#rt33",
        database="mydatabase"
    )
    return mydb

def closeMysqlConnection(mycursor):
    if mycursor:
        mycursor.close()
        print("\nYour connection was successfully and it is closed now.")


def mysqlVersion():
    try:
        mydb = mysqlConnection()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT version()")
        result = mycursor.fetchone()
        print("your version of mysql is : ",result)
    except Error as e:
        print("You did not connect to the mysql database ): \nSome things went wrong." , format(e))
    else:
        closeMysqlConnection(mycursor)

def hospitalDetail(id):
    try:
        mydb = mysqlConnection()
        mycursor = mydb.cursor()
        sql = ("SELECT * FROM hospital WHERE Hospital_Id = %s")
        mycursor.execute(sql,(id,))
        result = mycursor.fetchall()
        print("printing hospital detail that you gave... \n")
        for i in result:
            print("hospital id is :",i[0])
            print("Hospital name is :",i[1])
            print("Bed count is :",i[2])
    except Error as e:
        print("You did not connect to the mysql database ): \nSome things went wrong." , format(e))
    else:
        closeMysqlConnection(mycursor)

def doctorDetail(id):
    try:
        mydb = mysqlConnection()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM Doctor WHERE Doctor_Id = %s"
        mycursor.execute(sql,(id,))
        result = mycursor.fetchall()
        print("printing doctor detail that you gave... \n")
        for i in result:
            print("Doctor id is :",i[0])
            print("Doctor name is :",i[1])
            print("Hospital id is :",i[2])
            print("Joining data was :",i[3])
            print("Speciality is :",i[4])
            print("Salary is : ",i[5])
            print("Experience is :",i[6])
    except Error as e:
        print("You did not connect to the mysql database ): \nSome things went wrong." , format(e))
    else:
        closeMysqlConnection(mycursor)

def pickDoctor(speciality,salary):
    try:
        mydb = mysqlConnection()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM doctor WHERE Speciality = %s AND Salary >= %s"
        mycursor.execute(sql,(speciality,salary))
        result = mycursor.fetchall()
        print("find the doctor that you wanting and printing it...\n")
        for i in result:
            print("Doctor id is :",i[0])
            print("Doctor name is :",i[1])
            print("Hospital id is :",i[2])
            print("Joining data was :",i[3])
            print("Speciality is :",i[4])
            print("Salary is : ",i[5])
            print("Experience is :",i[6],"\n")
    except Error as e:
        print("You did not connect to the mysql database ): \nSome things went wrong." , format(e))
    else:
        closeMysqlConnection(mycursor)

def getHospitalName(id):
    try:
        mydb = mysqlConnection()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM hospital WHERE Hospital_Id=%s"
        mycursor.execute(sql,(id,))
        result = mycursor.fetchall()
        return result[0][1]
    except Error as e:
        print("You did not connect to the mysql database ): \nSome things went wrong." , format(e))
    else:
        closeMysqlConnection(mycursor)

def hospitalDoctor(id):
    try:
        hospital_name = getHospitalName(id)
        mydb = mysqlConnection()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM doctor WHERE Hospital_Id = %s"
        mycursor.execute(sql,(id,))
        result = mycursor.fetchall()
        print(f"The doctors of ",hospital_name," is :")
        for i in result:
            print("Doctor id is :",i[0])
            print("Doctor name is :",i[1])
            print("Hospital id is :",i[2])
            print("Joining data was :",i[3])
            print("Speciality is :",i[4])
            print("Salary is : ",i[5])
            print("Experience is :",i[6],"\n")
    except Error as e:
        print("You did not connect to the mysql database ): \nSome things went wrong." , format(e))
    else:
        closeMysqlConnection(mycursor)

def getJoiningData(id):
    mydb = mysqlConnection()
    mycursor = mydb.cursor()
    sql = "SELECT Joining_Data FROM doctor WHERE Doctor_Id = %s"
    mycursor.execute(sql,(id,))
    result = mycursor.fetchone()
    return result[0]
def updateDoctorExperiance(id):
    try:
        import time
        Joining = getJoiningData(id)
        JoiningTime = time.strptime(Joining , "%Y-%m-%d")
        JoiningYear = time.strftime("%Y" , JoiningTime)
        now = time.ctime()
        r = time.strptime(now , "%a %b %d %H:%M:%S %Y")
        presentYear = time.strftime("%Y" , r)
        experience = int(presentYear) - int(JoiningYear)
        mydb = mysqlConnection()
        mycursor = mydb.cursor()
        print("Updating doctor s experience...")
        sql = "UPDATE doctor SET Experience = %s WHERE doctor_Id = %s"
        mycursor.execute(sql,(experience , id))
        mydb.commit()
        print("Done!")
    except Error as e:
        print("You did not connect to the mysql database ): \nSome things went wrong." , format(e))
    else:
        closeMysqlConnection(mycursor)
