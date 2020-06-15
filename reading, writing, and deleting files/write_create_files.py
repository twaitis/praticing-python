# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

"""
file = open('intro.txt', 'a')
file.write('\nI will be ritch')
file.close()


file = open('intro.txt', 'r')
print(file.read())

# Open the file "demofile3.txt" and overwrite the content:

file = open('intro.txt', 'w')
file.write('My name is Sam Twaiti \nI will be rich one day. \nI am a Computer Scientist and a Linguist. \nI will find a good paying job in Yemen')
file.close()

file = open('intro.txt', 'r')
print(file.read())
"""
"""
#creating a new file and writing in it
file = open('second_wife.txt', 'x')
file.close

file = open('second_wife.txt', 'w')
file.write('Sabrin Weshah')
file.close()

file = open('second_wife.txt', 'r')
print(file.read())
"""
# To delete a file, you must import the OS module, and run its os.remove() function:
"""
import os
os.remove('second_wife.txt')
"""


"""
# Check if file exists, then delete it:
import os
if os.path.exists('second.txt'):
    os.remove('second.txt')
else:
    print('This files doesn\'t exists')
 """


# to remove a folder

import os
os.rmdir('bigdaddy')






