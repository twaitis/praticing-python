import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="twaitis",
  passwd="maram@060292"
)

print(mydb)
