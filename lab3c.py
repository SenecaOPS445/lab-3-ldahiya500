#!/usr/bin/env python3
#Author ID = lakshay2@myseneca.ca
#Author = lakshay2

Error = 'Error: function operator can be "add", "subtract", or "multiply"'
def operate(number1, number2, operator):
    if operator == "add":
        return int(number1) + int(number2)
    elif operator == "subtract":
        return int(number1) - int(number2) 
    elif operator == "multiply":
        return int(number1) * int(number2)
    elif operator == "divide":
        return Error


if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))