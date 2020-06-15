"""
a = lambda a: a + 10

print(a(5))
"""

"""
x = lambda a, b, c: a+b+c

print(x(1,2,3))
"""


def calculators(n):
    return lambda c: n * c


my_doubler = calculators(2)
my_tripler = calculators(3)

integer = input('Enter an integer: ')


print('Double of ' +integer+ ' is : ' +str(my_doubler(int(integer))))
print('Triple of ' +integer+ ' is : ' + str(my_tripler(int(integer))))






