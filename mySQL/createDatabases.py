import mysql.connector as msc

mydb = msc.connect(
    host = 'localhost',
    user = 'twaitis',
    passwd = 'maram@060292'
    )

mycursor = mydb.cursor()

mycursor.execute('create database myDatabase')

