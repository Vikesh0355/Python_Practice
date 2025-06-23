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