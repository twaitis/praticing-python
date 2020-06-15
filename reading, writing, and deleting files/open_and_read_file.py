"""
File handling is an important part of any web application.
Python has several functions for creating, reading, updating,
and deleting files.

The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""
# opening a file and reading it
file = open('intro.txt', 'r')
print(file.read())

#  you can also specify how many characters you want to return:
# print(file.read(3))
# You can return one line by using the readline() method:
print(' ')
file = open('intro.txt', 'r')
print(file.readline())
print(' ')

# read the file line by line
file = open('intro.txt', 'r')
for x in file:
    print(x)

# It is a good practice to always close the file when you are done with it.

file.close()

    













 
