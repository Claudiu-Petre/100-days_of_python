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
