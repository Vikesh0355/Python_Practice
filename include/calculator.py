def calculator(fun, x, y):
    return fun(x, y)

operations = [
    lambda x, y: x + y,  # Sum
    lambda x, y: x - y,  # Subtract
    lambda x, y: x * y,  # Multiply
    lambda x, y: x / y   # Division
]

