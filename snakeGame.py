import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  

turtle.register_shape("trash.gif")
turtle.register_shape("gameOver.gif")
turtle.bgcolor('ivory')
gameOverPic = turtle.clone()
gameOverPic.shape('gameOver.gif')
gameOverPic.hideturtle()





turtle.turtlesize(1.5)
borderTurtle = turtle.clone()#size. 
borderTurtle.pensize(10)
borderTurtle.penup()
borderTurtle.hideturtle()
borderTurtle.goto(-300,300)
borderTurtle.pendown()
borderTurtle.goto(300,300)
borderTurtle.goto(300,-300)
borderTurtle.goto(-300,-300)
borderTurtle.goto(-300,300)
borderTurtle.penup
turtle.penup()
borderTurtle.hideturtle()

titleTurtle = turtle.clone()
titleTurtle.penup()
titleTurtle.goto(0,370)
titleTurtle.color('firebrick')
titleTurtle.write("Snake Game", move=True, align="center", font=('Comic Sans MS', 40, 'bold'))
titleTurtle.hideturtle()

scoreWordTurtle = turtle.clone()
scoreWordTurtle.penup()
scoreWordTurtle.goto(0,-370)
scoreWordTurtle.color('firebrick')
scoreWordTurtle.write("Score: ", move=True, align="right", font=('Comic Sans MS', 30, 'bold'))
scoreWordTurtle.hideturtle()

scoreTurtle = turtle.clone()
scoreTurtle.penup()
scoreTurtle.goto(0,-370)
scoreTurtle.color('firebrick')
scoreTurtle.write("0", move=False, align="left", font=('Comic Sans MS', 30, 'bold'))
scoreTurtle.hideturtle()


SQUARE_SIZE = 30
LENGTH = 1
speed=300

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
stone_pos = []
stone_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("circle")
snake.color("firebrick")
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)

for i in range(LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos += SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    stamp_ID1 = snake.stamp()
    stamp_list.append(stamp_ID1)
    

###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!


#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP

UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300


def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    #Update the snake drawing <- remember me later
    print("You pressed the up key!")

##2. Make functions down(), left(), and right() that change direction
#####WRITE YOUR CODE HERE!!
def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
     #Update the snake drawing <- remember me later
    print("You pressed the left key!")

def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
     #Update the snake drawing <- remember me later
    print("You pressed the down key!")

def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
     #Update the snake drawing <- remember me later
    print("You pressed the right key!")

turtle.onkeypress(up, UP_ARROW) # Create listener for up key

##3. Do the same for the other arrow keys
#####WRITE YOUR CODE HERE!!

turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()
#_____________________________________________________

#turtle.register_shape("trash.gif")
#turtle.register_shape("stone.png")
food = turtle.clone()
stone = turtle.clone()
#food.shape("trash.gif")
stone.shape("trash.gif")
food.shape("turtle")
food.color("green")
stone.shapesize(1.5)
food.shapesize(1.5)
def make_food():
    
    turtlesAngle = random.randint(0,360)
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(RIGHT_EDGE/SQUARE_SIZE)+1
    max_x=int(RIGHT_EDGE/SQUARE_SIZE)-1
    min_y=-int(UP_EDGE/SQUARE_SIZE)+1
    max_y=int(UP_EDGE/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated position

    food.penup()
    food.goto(food_x, food_y)
    food.left(turtlesAngle)
    stamp_ID=food.stamp()
    food_stamps.append(stamp_ID)
    
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    food_pos.append(food.pos())
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list

def make_stone():
    
    min_x=-int(RIGHT_EDGE/SQUARE_SIZE)+1
    max_x=int(RIGHT_EDGE/SQUARE_SIZE)-1
    min_y=-int(UP_EDGE/SQUARE_SIZE)+1
    max_y=int(UP_EDGE/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    stone_x = random.randint(min_x,max_x)*SQUARE_SIZE
    stone_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated position

    stone.penup()
    stone.goto(stone_x, stone_y)
    stamp_ID_x=stone.stamp()
    stone_stamps.append(stamp_ID_x)
    
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    stone_pos.append(stone.pos())


#_____________________________________________________
def move_snake():
    global food_stamps, food_pos, LENGTH, pos_list, speed, stone_stamps, stone_pos, STAMP_ID1
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    justEaten=False

    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved left!")

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5

    if len(food_stamps)<=5:
        make_food()

    if  LENGTH >= 50:
        if len(stone_stamps) <= 10:
            make_stone()
            
    elif LENGTH >= 40:
        if len(stone_stamps) <= 8:
            make_stone()

    elif LENGTH >= 32:
        if len(stone_stamps) <= 7:
            make_stone()
            
    elif LENGTH >= 26:
        if len(stone_stamps) <= 6:
            make_stone()

    elif LENGTH >= 20:
        if len(stone_stamps) <= 5:
            make_stone()

    elif LENGTH >= 15:
        if len(stone_stamps) <= 3:
            make_stone()
            
    elif LENGTH >= 10:
        if len(stone_stamps) <= 2:
            make_stone()

    elif LENGTH >= 8:
        if len(stone_stamps) <= 1:
            make_stone()
        
    #If snake is on top of food item
    if snake.pos() in food_pos:

        scoreTurtle.clear()
        scoreTurtle.write(str(LENGTH), move = False, align = "left", font=('Comic Sans MS', 30, 'bold'))

        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food       
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        justEaten = True
        print("You have eaten the food!")

        if speed <= 90:
            speed -= 1
        
        elif speed <= 150:
            speed -= 3

        else:
            speed -= 5

    else:
        justEaten = False

    if snake.pos() in stone_pos:
        borderTurtle.pencolor('firebrick')
        borderTurtle.speed(1)
        borderTurtle.pensize(12)
        borderTurtle.penup()
        borderTurtle.hideturtle()
        borderTurtle.goto(-300,300)
        borderTurtle.pendown()
        borderTurtle.goto(300,300)
        borderTurtle.goto(300,-300)
        borderTurtle.goto(-300,-300)
        borderTurtle.goto(-300,300)
        borderTurtle.penup
        turtle.penup()
        snake.hideturtle()
        food.hideturtle()
        stone.hideturtle()
        snake.clearstamps()
        food.clearstamps()
        stone.clearstamps()
        gameOverPic.showturtle()
        #turtle.write("You've eaten yourself! \n        Game Over \n           score: " + str(LENGTH), move=False, align="center", font=("Times", 40, "bold"))
        quit()
        
    



    
    
    if snake.pos() in pos_list[:-1]:
        borderTurtle.pencolor('firebrick')
        borderTurtle.speed(1)
        borderTurtle.pensize(12)
        borderTurtle.penup()
        borderTurtle.hideturtle()
        borderTurtle.goto(-300,300)
        borderTurtle.pendown()
        borderTurtle.goto(300,300)
        borderTurtle.goto(300,-300)
        borderTurtle.goto(-300,-300)
        borderTurtle.goto(-300,300)
        borderTurtle.penup
        turtle.penup()
        snake.hideturtle()
        food.hideturtle()
        stone.hideturtle()
        snake.clearstamps()
        food.clearstamps()
        stone.clearstamps()
        gameOverPic.showturtle()
        #turtle.write("You've eaten yourself! \n        Game Over \n           score: " + str(LENGTH), move=False, align="center", font=("Times", 40, "bold"))
        quit()
        

        
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    if justEaten == False:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    else:
        LENGTH += 1

    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    

## The next three lines check if the snake is hitting the 
## right edge.
    if new_x_pos >= RIGHT_EDGE:
        #turtle.bgcolor('firebrick')
        borderTurtle.pencolor('firebrick')
        borderTurtle.speed(1)
        borderTurtle.pensize(12)
        borderTurtle.penup()
        borderTurtle.hideturtle()
        borderTurtle.goto(snake.pos())
        borderTurtle.pendown()
        borderTurtle.goto(300,-300)
        borderTurtle.goto(-300,-300)
        borderTurtle.goto(-300,300)
        borderTurtle.goto(300,300)
        borderTurtle.goto(snake.pos())
        borderTurtle.penup
        snake.hideturtle()
        food.hideturtle()
        stone.hideturtle()
        snake.clearstamps()
        food.clearstamps()
        stone.clearstamps()
        gameOverPic.showturtle()
        turtle.penup()
        #turtle.write("You hit the edge! \n   Game Over \n     score: " + str(LENGTH), move=False, align="center", font=("Times", 40, "bold"))
        quit()
#
#     # You should write code to check for the left, top, and bottom edges.
#    #####WRITE YOUR CODE HERE
    if new_x_pos <= LEFT_EDGE:
        #turtle.bgcolor('firebrick')
        borderTurtle.pencolor('firebrick')
        borderTurtle.speed(1)
        borderTurtle.pensize(12)
        borderTurtle.penup()
        borderTurtle.hideturtle()
        borderTurtle.goto(snake.pos())
        borderTurtle.pendown()
        borderTurtle.goto(-300,300)
        borderTurtle.pendown()
        borderTurtle.goto(300,300)
        borderTurtle.goto(300,-300)
        borderTurtle.goto(-300,-300)
        borderTurtle.goto(snake.pos())
        borderTurtle.penup
        snake.hideturtle()
        food.hideturtle()
        stone.hideturtle()
        snake.clearstamps()
        food.clearstamps()
        stone.clearstamps()
        gameOverPic.showturtle()
        turtle.penup()
        #turtle.write("You hit the edge! \n    Game Over \n       score: " + str(LENGTH), move=False, align="center", font=("Times", 40, "bold"))
        quit()

    if new_y_pos >= UP_EDGE:
        #turtle.bgcolor('firebrick')
        borderTurtle.pencolor('firebrick')
        borderTurtle.speed(1)
        borderTurtle.pensize(12)
        borderTurtle.penup()
        borderTurtle.hideturtle()
        borderTurtle.goto(snake.pos())
        borderTurtle.pendown()
        borderTurtle.goto(300,300)
        borderTurtle.goto(300,-300)
        borderTurtle.goto(-300,-300)
        borderTurtle.goto(-300,300)
        borderTurtle.goto(snake.pos())
        borderTurtle.penup
        snake.hideturtle()
        food.hideturtle()
        stone.hideturtle()
        snake.clearstamps()
        food.clearstamps()
        stone.clearstamps()
        gameOverPic.showturtle()
        turtle.penup()
        #turtle.write("You hit the edge! \n     Game Over \n        score: " + str(LENGTH), move=False, align="center", font=("Times", 40, "bold"))
        quit()

    if new_y_pos <= DOWN_EDGE:
        #turtle.bgcolor('firebrick')
        borderTurtle.pencolor('firebrick')
        borderTurtle.speed(1)
        borderTurtle.pensize(12)
        borderTurtle.penup()
        borderTurtle.hideturtle()
        borderTurtle.goto(snake.pos())
        borderTurtle.pendown()
        borderTurtle.goto(-300,-300)
        borderTurtle.goto(-300,300)
        borderTurtle.goto(300,300)
        borderTurtle.goto(300,-300)
        borderTurtle.goto(snake.pos())
        borderTurtle.penup
        snake.hideturtle()
        food.hideturtle()
        stone.hideturtle()
        snake.clearstamps()
        food.clearstamps()
        stone.clearstamps()
        gameOverPic.showturtle()
        turtle.penup()
        #turtle.write("You hit the edge! \n     Game Over \n       score: " + str(LENGTH), move=False, align="center", font=("Times", 40, "bold"))
        quit()
        #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

                
    turtle.ontimer(move_snake,speed)


move_snake()


#_____________________________________________________________________________________






#_____________________________________________________________________________________
turtle.mainloop()
