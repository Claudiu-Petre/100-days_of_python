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
# or
while not at_goal():
    jump()
# or with extra conditions:
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Project: Reeborg's World - the robot(Hurdle 4)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Project: Reeborg's World - Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
       turn_right()
       move()
    elif front_is_clear():
        move()
    else:
       turn_left()



