from art import logo
import math 

def addition(n1,n2):
    return n1 + n2

def subtraction(n1,n2):
    return n1 - n2

def multiplication(n1,n2):
    return n1 * n2

def division(n1,n2):
    if not n2 == 0:
        return n1 / n2
    else:
        return math.inf()
def want_continue():
    want = input("Do you want to continue: 'y' or 'n', or 'new'>>>")
    if want.lower() == 'y':
        return True
    elif want.lower() == 'n':
        return False
    else: 
        return "new"
print(logo)
print("Calculator starts...")

def calculator():
    is_continue = True
    while is_continue:
        number1 = float(input("Enter the first number>>>"))
        number2 = float(input("Enter the second number>>>"))
        operations = {"*":multiplication, "/":division,"+":addition,"-":subtraction}
        for k in operations:
            print(k)
        operation_symbol = input("Please choose one of the operations above>>>")
        operation = operations[operation_symbol]
        result = operation(number1,number2)
        print(f"{number1} {operation_symbol} {number2} = {result}")
        is_continue = want_continue()
        while is_continue: 
            number = float(input("Enter new number>>>"))
            operation_symbol = input("Choose your operation type>>>")
            operation = operations[operation_symbol]
            result= operation(result,number)
            print(f"{result} {operation_symbol} {number} = {result}")
            is_continue = want_continue()
            if is_continue =="new":
                calculator()

calculator()

