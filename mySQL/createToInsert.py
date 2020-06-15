import mysql.connector as msc

mydb = msc.connect(
    host='localhost',
    user='twaitis',
    passwd='maram@060292'
    )

mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE mydatabase')

mydb = msc.connect(
    host='localhost',
    user='twaitis',
    passwd='maram@060292',
    database='mydatabase'
    )
mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE customers(ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY, firstName VARCHAR(30) NOT NULL, address VARCHAR(30))')

sql = 'INSERT INTO customers(firstName, address) VALUES(%s, %s)'
val = [
    ('Sam', 'Wilson, NC'),
    ('Maram', 'Wilson, NC'),
    ('Sabrin', 'Greenville, NC'),
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
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
    ]

mycursor.executemany(sql, val)

mydb.commit()

print('The number of records inserted: ', mycursor.rowcount)
print(' ')
print('ID of last record inserted: ', mycursor.lastrowid)
