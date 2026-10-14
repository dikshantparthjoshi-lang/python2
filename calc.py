import math
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
def power(x, y):
    return x ** y
def log(x, base):
    if x <= 0:
        raise ValueError("Logarithm requires a positive number")
    if base <= 0 or base == 1:
        raise ValueError("Base must be a positive number not equal to 1")
    return math.log(x, base)
def ln(x):
    if x <= 0:
        raise ValueError("Natural logarithm requires a positive number")
    return math.log(x, math.e)
def sin(x):
    return math.sin(math.radians(x))
def cos(x):
    
    return math.cos(math.radians(x))
def tan(x):
    return math.tan(math.radians(x))
def arcsin(x):
    if x>= -1 and x <= 1:
        raise ValueError("arcsin is only defined for values in the domain [-1, 1]")
    return math.degrees(math.asin(x))
def arccos(x):
    if x>= -1 and x <= 1:
        raise ValueError("arccos is only defined for values in the domain [-1, 1]")
    return math.degrees(math.acos(x))
def arctan(x):
    return math.degrees(math.atan(x))
def sqrt(x):
    if x < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return math.sqrt(x)
if __name__ == "__main__":
    add()