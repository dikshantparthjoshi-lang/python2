import math

t = input("open/close calculator:").strip().lower()
while t not in ["open", "close"]:
    print("Please enter a valid option: 'open' or 'close'.")
    t = input("open/close calculator:").strip().lower()
if t == "open":
    # 🔁 The loop is inside the "open" block
    while True:
        while True:
            try:
                x = float(input("Enter a number: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        while True:
            try:
                y = float(input("Enter another number: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        while True:
            operator = input("enter the operator(+,*,/,-,power(xʸ),tan,sin,cos,log,ln,arctan,arcsin,arccos,sqrt,cust_log):").strip().lower()
            if operator in ['+', '-', '*', '/', 'power(xʸ)', 'tan', 'sin', 'cos', 'log', 'ln','arctan','arcsin','arccos','sqrt','cust_log']:
                break
            else:
                print("Please enter a valid operator.")
    
        if operator == '+':
            print(x+y)
        elif operator == "-":
            print(x-y)
        elif operator == "/":
            try:
                print(x/y)
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
        elif operator == "*":
            print(x*y)
        elif operator == "power(xʸ)":
            print(x**y)
        elif operator == "tan":
            print(math.tan(math.radians(x)))
        elif operator == "cos":
            print(math.cos(math.radians(x)))
        elif operator == "sin":
            print(math.sin(math.radians(x)))
        elif operator == "log":
            try:
                print(math.log10(x)) # Note: standard log is base 10
            except ValueError:
                print("Error: Logarithm is not defined for non-positive numbers.")  
        elif operator == "ln":  # Fixed: changed from 'else operator == "ln"' to 'elif'
            try:
                print(math.log(x, math.e)) 
            except ValueError:
                print("Error: Logarithm is not defined for non-positive numbers.")
        elif operator == "arctan":
            print(math.degrees(math.atan(x)))  
        elif operator == "arcsin":
            print(math.degrees(math.asin(x)))  
        elif operator == "arccos":
            print(math.degrees(math.acos(x)))
        elif operator == "cust_log":
            base = float(input("Enter the base for custom logarithm: "))
            if isinstance(base, (int, float)) and base <= 0:
                print("Error: Logarithm requires a positive base.")
                continue
            try:
                print(math.log(x, base))  
            except ValueError:
                print("Error: Logarithm is not defined for non-positive numbers")  
        elif operator == "sqrt":
            try:
                print(math.sqrt(x))  
            except ValueError:
                print("Error: Square root is not defined for negative numbers.")
        # To make a loop run forever until told otherwise, 
        # we check inside the loop if the user wants to stop.
        ask_again = input("Do you want to continue? (yes/no): ").strip().lower()
        if ask_again == 'no':
            print("Closing calculator...")
            break

# ➡️ This aligns perfectly with the 'if t == "open":' statement above!
elif t == "close":
    print("Calculator closed immediately.") # Changed 'break' to a print because there is no loop here
