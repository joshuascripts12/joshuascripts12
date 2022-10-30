
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

##### OPERATORS


