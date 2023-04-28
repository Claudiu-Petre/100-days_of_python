# Conditional Statements; Logical Operators; Code block and Scope

# IF / ELSE
    # Modulo: odd or even
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print ('This is an even number')
else:
    print('This is an odd number')

# Nested if/elif/else
height = int(input('What is your height in cm? '))
if height >= 120:
    print('You can ride')
    age = int(input('What is your age? '))
    if age < 12:
        print('Please pay $5')
    elif (age <= 18):
        print('Please, pay 7$')
    else:
        print('Please pay $12')
else:
    print('Sorry, grow up!')

# Challenge: BMI with interpretation
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f'Your bmi is {bmi}, you are underweight')
elif bmi < 25:
    print(f'Your bmi is {bmi}, you have a normal weight')
elif bmi < 30:
    print(f'Your bmi is {bmi}, you are slightly overweight')
elif bmi < 35:
    print(f'Your bmi is {bmi}, you are obese')
else:
    print(f'Your bmi is {bmi}, you arr clinically obese')