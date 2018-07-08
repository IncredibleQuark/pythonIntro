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

# curly brackets {} are for defining a dictionary
print({"name": "George", "age": 30, "hobby": "coding"})
