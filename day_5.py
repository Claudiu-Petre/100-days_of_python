# LOOPS

  # FOR
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")

print(fruits)

# Challenge: calc the average height
# Don't use sum() and len()
student_heights = input("Input a list of student heights ").split()
    # returns a list of integers
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_height = 0
count_no_height = 0
    # returns the sum of heights 
for height in student_heights:
    sum_height += height
    # returns the number of students
for student in student_heights:
    count_no_height += 1

# print(sum_height, count_no_height)
average = round(sum_height / count_no_height)
print(average)

# Challenge: write a program that calculates the highest score from a List of scores.
# don't use the max() or min()
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

res = 0
for score in student_scores:
    if(score > res):
        res = score
print(f'The highest score in the class is: {res}')

  # FOR with RANGE (doesn't include the last digit)
result = 0
for number in range (1, 101):
   result += number
print(result)

# change the pace by 2, etc:
result = 0
for number in range (1, 101, 2):
   result += number
print(result)

# Challenge: You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100:
total = 0
for number in range (1, 101):
    if number % 2 == 0:
        total += number
print (total)
# OR
total = 0
for number in range (2, 101, 2):
  total += number
print (total)

# Challenge: FizzBuzz
for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print (number)

# Challenge: Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for c in range(1, nr_letters + 1):
  password += random.choice(letters)

for s in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for num in range(1, nr_numbers + 1):
  password += random.choice(numbers)
  
print(password)



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

final = '' .join(random.sample(password, len(password)))
print(final)