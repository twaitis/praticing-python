import mysql.connector as msc

mydb = msc.connect(
    host='localhost',
    user='twaitis',
    passwd='maram@060292',
    database='mydatabase'
    )

mycursor = mydb.cursor()

#mycursor.execute('CREATE TABLE user(id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(30), fav INT)')

#mycursor.execute('CREATE TABLE products(id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(30))')


sql = 'INSERT INTO user (id, name, fav) VALUES (%s, %s, %s)'
val = [
    ('John', 154),
    ('Peter', 154),
    ('Amy', 155),
    ('Hannah', ),
    ('Michael', )
    ]

mycursor.executemany(sql, val)

mydb.commit()
