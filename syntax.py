# STRINGS

print('hello')

print("5" + "5")  # will return string '55'

print(int("5") + int("5"))  # cast the strings to get proper result

#  print("I am " + 99 + "years old")  # will return error can't convert int object to string

print("I have " + str(200) + " dollars.")  # have to cast int into a string to add it properly

print("Hello:World".split(":"))  # returns an array of strings separated by ':'


# BOOLEANS

print(5 == 5)
print(5 is 5)
print(4 is not 4)  # evaluates to false
print("Word" is "Word")
print("True" is True)  # 'is' checks also for types so it will be false


# ARRAYS (LISTS)

print("I am " + ["John", "George", "Steven"][1])  # accessing array

print({"name": "George", "age": 30, "hobby": "coding"})  # curly brackets {} are for defining a dictionary


# VARIABLES

greeting = "Hello"
print(greeting)
print(greeting + " John")
number = 3
print(number * 5 + 2)


# BUILT-IN FUNCTIONS
# str(), int(), bool()

print(len('Hello'))
print(len([1, 4, 5]))

array = [14, 5, 7, 90, 22, 44, 4, 2, 73]
print(sorted(array))
stringsArray = ["R", "S", "a", "c", "w", "e", "T", "G", "7", "8.1", "3.3"]
print(sorted(stringsArray))  # it sorts numbers as strings first, then capital letters, then normal letters


# FUNCTIONS

def my_function():  # key word, name of the function which should be written in snake_case and colon ':' at the end
    print("Calling my function")


my_function()


def print_arguments(word="Some number: ", count=155):  # setting default parameters
    print(word)
    print(count)


print_arguments("You can see a number below: ", 144)
print_arguments("Using default number: ")
print_arguments(count=200)


def print_people(*people):  # infinite number of arguments
    for person in people:
        print("This person is " + person)


print_people("John", "Mark", "Ella", "Janna", "Oho")


def do_math(num1, num2):
    return num1 + num2


result = do_math(5, 6)
print(result)


# IF ELSE

check = "Good"

if check == True:
    print("It is true!")
elif check == "Good":
    print("It is good")
else:
    print("It is false")


# LOOPS

numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print(item)


run = True
current = 1

while run:
    if current == 11:
        run = False
    else:
        print("Going up ", current)
        current += 1


# IMPORTING LIBRARIES

import re  # REGEX library

sentence = "I like to program in Python VERY MUCH!!!!!!!"
new = re.sub('[A-Z!]', '', sentence)  # remove all capital letters and !

print(new)
sentence = sentence + "333556"
print(sentence)
new = re.sub('[0-9]', '*', sentence)
print(new)
