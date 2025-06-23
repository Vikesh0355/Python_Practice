def swap(a, b):
    a = a+b;
    b = a-b;
    a = a-b;
    return a, b;

a = 10
b = 20
a, b = swap(a, b)
print("value of a after swap: ", a)
print("Value of b after swap: ", b)


#print particular char from string
var = "Vikesh"
print(var[4])
# Print letters from 0th to 4th index
for i in range(5):
    print(var[i])

