import mysql.connector as msc

# create a database named mydatabase
"""
mydb = msc.connect(
    host='localhost',
    user='twaitis',
    passwd='maram@060292'
    )

mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE mydatabase')
"""

# in mydatabase database, create a tables named customers
# create 3 columns (id, firstName, lastName)
# makes sure that ID is the primary key of the table

mydb = msc.connect(
    host='localhost',
    user='twaitis',
    passwd='maram@060292',
    database='mydatabase'
    )

mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE customers(ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY, firstName VARCHAR(30), lastName VARCHAR(30))')

