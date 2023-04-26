# Data types
# Strings - subscripting
print("Hello"[0])

# Integer
print(123 + 456 + 789_876)

# Float
print(3.123 + 123_456)

# Boolean
True
False

# type function to check the data type
char = input("What is your name?")
print(type(len("Your name has" + char + "characters")))

            # Conversions
# Integers - strings
char = len(input("What is your name?"))
new_char = str(char)
print(len("Your name has" + new_char + "characters"))

# Other conversions
a = str(123)
print(type(a)) // string
print( 70 + float("100.6")) // 170.6
print (str(70) + str(100)) // 70100

# Challenge: Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
number = input("Type a two digit number: ")
first_digit = int(number[0])
second_digit = int(number[1])
result = first_digit + second_digit
print(result)

# Mathematical operations
3 + 5
7 - 6
2 * 4
print(6 / 2) // float result
2 ** 2 (3, ..) // exponential (to the power of 2, 3, etc)

    # PEMDAS LR: 
    # ()parentheses, 
    # ** exponential, 
    # * multiplication, 
    # / division, 
    # + addition, 
    # - subtraction
    # LR left to right
print(3 * 3 + 3 / 3 - 3) // 7
# Change the above to obtain 3.0
print(3 * (3 + 3) / 3 - 3) // 3

# Challenge: calculate BMI = weight / 2*height
height = input('enter your height in m: ')
weight = input('enter your weight in kg: ')

bmi = weight / float(height) **2
bmi_integer =  int(bmi)
print(bmi_integer)

# Rounding
print(round(8 / 3)) // 2.6666 = 3
print(round(8 / 3, 2)) // 2.6666 = 2.67 (2 decimal points)

print(8 // 3) // flow division gives you an ROUNDED INTEGER

# keeping and updating scores..
score = 0
score += 1
score -= 1
score *= 1
score /= 1

print(score) // 1

#  F strings
score = 0
height = 1.75
isSwimming = True

print(f'your score is {score}, your height is {height} and you can swim {isSwimming}')
