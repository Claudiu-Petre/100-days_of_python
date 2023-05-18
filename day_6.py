# Functions
    # create your own function:
def my_function():
    print('Hello')
    print('Bye')
my_function()

#  Challenge: Reeborg's World
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()

# Code Blocks - Indentation
    # 4 spaces = 1 tab
    # official recommendation: 4 spaces

# While loop 
nr_loops = 6    
while nr_loops > 0:
    jump()
    nr_loops -= 1

while at_goal() != True:
    jump()

# Project: Karel the robot




