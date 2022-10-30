
##### 

myint = 7 # int - integer, a whole number
print(myint)

myfloat = 7.0 # float - floating point number, decimal
print(myfloat)
# OR, you can also define a floating point number by running..
myfloat = float(7)
print(myfloat)

# a string is defined with single or double quotes
mystring = 'hello'
print(mystring)

# you should use double quotes when your string has apostrophes

##### MATHEMATICS

one = 1
four = 4
five = one + four
print(five)

##### STATEMENTS

kalistus = "kalistus"
oo = "oo"
kalistusoo = kalistus + " " + oo
print(kalistusoo)

# you can run 2 assignments on one variable, however you may NOT mix numbers and strings..

a, b = 3, 4
print(a,b)

## EXERCISE

mystring = 'hello'
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

##### LISTS

# this code adds 1
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

# you may not access an index which does not exist
# example: if your list is 1, 2 and 3 you may not print 10 from your list.

## EXERCISE

numbers = [1,2,3]
strings = ['hello', 'world']
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

##### OPERATORS - come back

number = 1 + ((2 * 3) / 4.0)
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

weighingchicken = "kalistus" + " " + "and" + " " + "chicken"
print(weighingchicken)

lotsofnairastolen = "i need to pay for medical fees! " * 5
print(lotsofnairastolen)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

## EXERCISE 

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

##### STRING FORMATTING

# python string formatting is C-style
# % operator formats a set of variables enclosed in a tuple
# a tuple is a fixed size list
# a format string contains normal text with argument specifiers
# a specifier can be %s or %d

name = "Kalistus Akpolla"
print("Hello, %s!" % name)

# to use 2 or more argument specifiers, use a tuple (parentheses)

name = "Bomalistical Wike"
age = 69
home = "Abuja"
print("%s is %d years old and lives in %s." % (name, age, home))

# %s - strings, %d - integers, %f - floating point numbers

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# %s can also be used for lists

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)








