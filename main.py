from replit import clear 
from art import logo
#To add nos.
def add(n1,n2):
    """This function takes two arguments to add numbers """
    return n1+n2


#To subtract 
def subtract(n1,n2):
    """This function takes two arguments to subtract numbers """
    return n1-n2

#To multiply
def multiply(n1,n2):
    """This function takes two arguments to multiply numbers """
    return n1*n2

#To divide
def divide(n1,n2):
    """This function takes two arguments to divide numbers """
    return n1/n2


operations = { 
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    }
print(logo)
def calculator():
    num1 = float(input("Enter first number: "))
    while True:
        for key in operations:
           print(f'"{key}"')
        operation_symbol = input("Pick an operation from the above list: ")
        num2 = float(input("Enter the second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to calculating with {answer} or Type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            clear()
            calculator()
calculator()
        
