# ~ complement ooperator: if we use this like ~Number it will give result = -(number+1). It is same like c
#identity Operator: The identity operator in Python is used to compare the memory locations of two objects. There are two identity operators:

#is: Returns True if the variables on either side of the operator point to the same object.
#is not: Returns True if the variables on either side of the operator do not point to the same object.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, because b points to the same object as a
print(a is c)  # False, because c is a different object with the same content
print(a is not c)  # True, because c is not the same object as a

#another example
a =5
b =5
print("\n")
print(id(a))
print(id(b))
print(a is b)
print("\n")

#membership operator: In Python, the membership operators "in" and "not in" are used to test whether a value is a member of a sequence (such as a string, list, tuple, or set) or a dictionary. Here's a quick overview of how they work:
# Example with a list
fruits = ["apple", "banana", "cherry"]
print("orange" in fruits)  # Output: FALSE
print("\n")

# Example with a string
text = "Hello, world!"
print("world" in text)  # Output: True
print("\n")


print(round(3.14159))  # Output: 3
print(round(2.71828))  # Output: 3

print(round(3.14159, 2))  # Output: 3.14
print(round(2.71828, 3))  # Output: 2.7187
print(round(7.41)) #output 7
print(round(7.5)) #output 8
print(round(6.5)) #output 6, generally it return nearest even integer in such case
print(round(674, -1)) #output 670, here it print the multiple of 10 but closest to the number so 670 is closest multiple if 671.
print(round(574, -2)) #output 600, here make first two digit to 0 , then increment the first digit by 1
print(round(674, -3)) #output 1000, since here we pass -3 as 2nd argument so it will print closest multiple of 1000
print(round(665, -1)) #output 600, nearest even integer and multiple of 10
print(round(675, -1)) #output 680, nearest even integer and multiple of 10