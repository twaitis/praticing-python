import mysql.connector as msc

mydb = msc.connect(
    host='localhost',
    user='twaitis',
    passwd='maram@060292',
    database='mydatabase'
    )

mycursor = mydb.cursor()

mycursor.execute('SELECT firstName, Address FROM customers where Address = "Greenville, NC"')

myResult = mycursor.fetchall()

for x in myResult:
    print(x)

    
