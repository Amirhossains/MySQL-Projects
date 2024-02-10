import mysql.connector
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename , 'rb') as file:
        binaryData = file.read()
    return binaryData
def insertBOLB(emp_id , name , photo , biodataFile):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Amir#rt33",
        database="mydatabase"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO `Python_Employee` (id , name , photo , biodata) VALUES (%s,%s,%s,%s)"
    empPicture = convertToBinaryData(photo)
    file = convertToBinaryData(biodataFile)
    val = (emp_id , name , empPicture , file)
    mycursor.execute(sql,val)
    mydb.commit()
insertBOLB(18 , "Eric" , "C:\sun.JPEG" , "C:\Read.Text")