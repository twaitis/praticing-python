# insert Sam Twaiti as first and last name for one record

import mysql.connector as msc

mydb = msc.connect(
    host='localhost',
    user='twaitis',
    passwd='maram@060292',
    database='mydatabase'
    )
mycursor = mydb.cursor()

"""

sql = 'INSERT INTO customers(firstName, lastName) VALUES(%s, %s)'
val = ('Sam', 'Twaiti')

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, 'record inserted.')

# Important!: Notice the statement: mydb.commit(). It is required to make the
# changes, otherwise no changes are made to the table.

"""

"""
To insert multiple rows into a table, use the executemany() method.

The second parameter of the executemany() method is a list of tuples, containing
the data you want to insert:
"""

# Fill the "customers" table with data:
"""

sql = 'INSERT INTO customers(firstName, lastName) VALUES(%s, %s)'
val = [
    ('Maram', 'Abdo'),
    ('Sabrin', 'Weshah'),
    ('Mohamed', 'Moharem'),
    ('Amanda', 'King'),
    ('Ashton', 'Rueda'),
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989')
    ]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, 'records inserted.')

"""

# Insert one row, and return the ID:

sql = 'INSERT INTO customers(firstName, lastName) VALUES(%s, %s)'
val = ('Alexanderia', 'Coolwoman')

mycursor.execute(sql, val)

mydb.commit()

print('The ID of the last person was added is: ', mycursor.lastrowid)
























