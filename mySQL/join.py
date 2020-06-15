import mysql.connector as msc

mydb = msc.connect(
    host='localhost',
    user='twaitis',
    passwd='maram@060292',
    database='mydatabase'
    )

mycursor = mydb.cursor()

# Join users and products to see the name of the users favorite product:
# inner join
"""
sql = 'SELECT\
    user.name as Name, \
    products.name as Favorite \
    FROM user INNER JOIN products \
    ON user.fav = products.id'

mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)

"""

# Select all users and their favorite product:
# left join
"""
sql = 'SELECT \
    user.name AS user, \
    products.name AS favorite \
    FROM user LEFT JOIN products \
    ON user.fav = products.id'

mycursor.execute(sql)
result = mycursor.fetchall()
for x in result:
    print(x)
"""
# Select all products, and the user(s) who have them as their favorite:

sql = 'SELECT user.name AS user, products.name AS Favorite \
    FROM user RIGHT JOIN products \
    ON user.fav = products.id'

mycursor.execute(sql)
result = mycursor.fetchall()
for x in result:
    print(x)

    
