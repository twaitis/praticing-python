import mysql.connector as msc

# Select all records from the "customers" table, and display the result:

mydb = msc.connect(
    host='localhost',
    user='twaitis',
    passwd='maram@060292',
    database='mydatabase'
    )

mycursor = mydb.cursor()

mycursor.execute('SELECT* FROM customers')

myResult = mycursor.fetchall()

for x in myResult:
    print(x)

print(' ')
    
# Select only the name and address columns:

mycursor.execute('SELECT firstName, address FROM customers')

myResult = mycursor.fetchall()

for x in myResult:
    print(x)
    
"""
The fetchone() method will return the first row of the result:

"""
# Fetch only one row:
mycursor.execute('SELECT* FROM customers')
myResult = mycursor.fetchone()

for x in myResult:
    print(x)
