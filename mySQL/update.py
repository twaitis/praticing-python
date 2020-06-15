import mysql.connector as msc

mydb = msc.connect(
    host='localhost',
    user='twaitis',
    passwd='maram@060292',
    database='mydatabase'
    )

mycursor = mydb.cursor()

"""
# Overwrite the address column from "Valley 345" to "Canyoun 123":

sql = 'UPDATE customers SET address = "Canyon 123" WHERE address = "Valley 345"'

mycursor.execute(sql)

mydb.commit()

print('record(s) affected: ', mycursor.rowcount)
"""

# Escape values by using the placholder %s method:

sql = 'UPDATE customers SET address = %s WHERE address = %s'
val = ('Valley 345', 'Canyon 123')

mycursor.execute(sql, val)

mydb.commit()


