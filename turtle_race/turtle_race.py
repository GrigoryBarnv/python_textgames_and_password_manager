import turtle 
import time

WIDTH, HEIGHT = 500, 500 # turtle constant monitor values

screen = turtle.Screen() # initialize turtle screen
screen.setup(WIDTH, HEIGHT)
screen.title('Turtle_racing')


def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 -10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try Again!')
            continue 
        
        if 2 <= racers <= 10: # check weather the racers are in the range 
            return racers
        else:
            print('Number in range 2-10, Try again! ')


racers = get_number_of_racers()
init_turtle()

racer = turtle.Turtle()
racer.forward(100)
time.sleep(5)
