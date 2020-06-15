"""
You can limit the number of records returned from the query, by using the
"LIMIT" statement:
"""
import mysql.connector as msc

mydb = msc.connect(
    host='localhost',
    user='twaitis',
    passwd='maram@060292',
    database='mydatabase'
    )

mycursor = mydb.cursor()

# Select the 10 first records in the "customers" table:

sql = 'SELECT * FROM customers LIMIT 10'

mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)

print(' ')

"""
If you want to return five records, starting from the third record, you can
use the "OFFSET" keyword:
"""

# Start from position 5, and return 5 records:

sql = 'SELECT * FROM customers LIMIT 5 OFFSET 4'

mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)
    



