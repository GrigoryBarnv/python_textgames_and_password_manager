import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['green', 'orange', 'yellow', 'black', 'purple', 'cyan', 'blue', 'red', 'pink', 'brown']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try Again!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2-10. Try Again!')

def race(colors):
    turtles = create_turtles(colors) # create all turtles inside the function 

    while True: # repeat till the turtle gets to the top of the screen 
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)] # return means that the loop will be stopped as soon as a condition is reachd 

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1) 
    for i, color in enumerate(colors): # enumereate -> get index and value 
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i +1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()

colors = random.sample(COLORS, racers)

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)
