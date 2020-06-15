countries = ['Yemen', 'USA', 'Syria', 'Saudi Arabia']
a = ['UK', 'UAE']

c = countries.copy()


# c.append('Italy')
# c.clear()
# print(c.count('Yemen'))




# python does not have a built in array, but python list can be used instead

for x in c:
    if x == 'Yemen':
        print('Great Yemen, the country of Sam')
    elif x == 'USA':
        print('Great America')
    elif x == 'Saudi Arabia':
        print('I don\'t know where the Saudies are going')
    else:
        print(x)
