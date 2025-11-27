#1 The goal is to create a simple calculator
import math
print('Welcome to the python calculator!')
print('If you wish to see what operations are possible please enter: \"operations\" or \"o\"')

#3 Make the calculator allows an input until its terminated
print('If you wish to close the calculator please enter \"end\" or \"e\"')
calc_on = True
while calc_on:

#2 Need to create a menu that the user can access showcasing all the functionalities of the calculator
    calculate: str = input('Please enter a calculation in the form \"x\" \"operator\" \"y\": ').lower()

#6 Adding incorrect input help
    valid_input = False
    while valid_input == False:
        calc_parts = calculate.split(' ')
        if calculate in ['operations', 'o', 'end', 'e',]:
            valid_input = True
        elif len(calc_parts) == 3 and type(float(calc_parts[0])) == float and type(str(calc_parts[1])) == str and type(float(calc_parts[2])) == float:
            valid_input = True
        else:
            valid_input = False
            calculate: str = input('Sorry, please ensure you enter a calculation in the form \"x\" \"operator\" \"y\": ').lower()
    if calculate in ['end', 'e']:
        calc_on = False
    elif calculate in ['operations', 'o']:
        print('This is a comprehensive list of all the operations you can perform. \nThis list is in the following format: \"operator\", \"symbol\"')
        print('Addition, +\nSubtraction, -\nMultiplication, *\nDivision, /\nExponential, ^\nSquare root, sqrt()')

#3 Splitting the inputs so the calculator can interpret each character individually
    else:
        calc_parts = calculate.split(' ')
        num1 = float(calc_parts[0])
        operator = str(calc_parts[1])
        num2 = float(calc_parts[2])
#4 Creating addition functionality
        if operator == '+':
            print(f'{num1} + {num2} = {num1 + num2}')
#5 Creating subtraction functionality
        if operator == '-':
            print(f'{num1} - {num2} = {num1 - num2}')
print('Thank you for using the calculator, goodbye!')
