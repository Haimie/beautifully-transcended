valid_options=['add', 'subtract', 'divide', 'multiply']

operation=input('What operation would you like to do?\n''(the valid operations are "add", "subtract", "divide", "multiply"):\n')
if operation not in valid_options:
    print('Invalid choice')
    exit(-1)

number1=input('Enter the first number: ')
number2=input('Enter the second number: ')
if number1.isalpha() or number2.isalpha():
    print('You should only input numeric values!')
    exit(-1)


number1=float(number1)
number2=float(number2)

answer= 0
if operation=="add":
    answer=number1+number2
elif operation=="subtract":
    answer=number1-number2
elif operation=="divide":
    answer=number1/number2
elif operation=="multiply":
    answer=number1*number2
print('The answer is:', answer)

