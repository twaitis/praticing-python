"""
Use the ORDER BY statement to sort the result in ascending or descending order.

The ORDER BY keyword sorts the result ascending by default. To sort the result in
descending order, use the DESC keyword.
"""

import mysql.connector as msc

mydb = msc.connect(
    host='localhost',
    user='twaitis',
    passwd='maram@060292',
    database='mydatabase'
    )

mycursor = mydb.cursor()

# Sort the result alphabetically by name:

sql = 'SELECT* FROM customers ORDER BY firstName'

mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)

# in a descendant order, Sort the result alphabetically by name:

sql = 'SELECT* FROM customers ORDER BY firstName DESC'

mycursor.execute(sql)

result = mycursor.fetchall()
print(' ')
for x in result:
    print(x)
    
    
