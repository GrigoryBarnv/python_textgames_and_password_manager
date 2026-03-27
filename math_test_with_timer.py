import random
import time 

OPERATORS = ["+", "-", "*"]
MAX_OPERAND = 12
MIN_OPERAND = 3
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr) # evaluate the expression
    return expr, answer






wrong = 0
input("Press enter to start")
print("-------------------------")


start_time = time.time()  # mark the starttime 

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem # " + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer): # cannot compare string and integer even if 10 = '10'
            break
        wrong += 1
        
        
end_time = time.time()
total_time = round(end_time - start_time, 2)
        
print("---------------")
print("nice work, you finishced in ", total_time , "seconds !")