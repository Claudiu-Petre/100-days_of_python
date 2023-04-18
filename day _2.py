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