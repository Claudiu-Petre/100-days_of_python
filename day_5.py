# LOOPS

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
