import mysql.connector as msc

# Select record(s) where the address is "Park Lane 38": result:


mydb = msc.connect(
    host='localhost',
    user='twaitis',
    passwd='maram@060292',
    database='mydatabase'
    )

mycursor = mydb.cursor()

mycursor.execute('SELECT* FROM customers WHERE address = "Wilson, NC"')

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

"""
You can also select the records that starts, includes, or ends with a given
letter or phrase.
Use the %  to represent wildcard characters:
"""

# Select records where the address contains the word "ville":

sql = 'SELECT* FROM customers WHERE address LIKE "%ville%"'

mycursor.execute(sql)

result = mycursor.fetchall()
print(' ')
for x in result:
    print(x)
    
# Escape query values by using the placholder %s method:
sql = 'SELECT* FROM customers WHERE firstName = %s'
firstname = ('Hannah', )

mycursor.execute(sql, firstname)

result = mycursor.fetchall()

for x in result:
    print(' ')
    print(x)
