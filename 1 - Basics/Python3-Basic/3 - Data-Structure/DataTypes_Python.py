
"""

There are eight native datatypes in Python.

Boolean
Numbers
Strings
Bytes & Byte Arrays
Lists
Tuples
Sets
Dictionaries

Let us look at how to implement these data types in Python.
"""

#Boolean
number = [1,2,3,4,5]
boolean = 3 in number
print(boolean)
 
#Numbers
num1 = 5**3
num2 = 32//3
num3 = 32/3
print('num1 is',num1)
print('num2 is',num2)
print('num3 is',num3)
 
#Strings
str1 = "Welcome"
str2 = " to python "
str3 = str1 + str2
print('str3 is',str3)
print(str3[0:10])
print(str3[-5:])
print(str3[:-5])
 
#Lists
name = ['yassine', 'ahmed', 'sofyan']
print(len(name))
print(name)
name.append('yassine')
print(name)
name.insert(2, 'ahmed')
print(name)

 
#Tuples
sports_tuple = ('Cricket', 'Basketball', 'Football')
sports_list = list(sports_tuple)
sports_list.append('Baseball')
print(sports_list)
print(sports_tuple)
 
