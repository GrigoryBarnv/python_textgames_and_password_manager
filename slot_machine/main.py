
import random

MAX_LINES = 3  # global constant, not posssible to change 
MAX_BET = 100
MIN_BET = 3 

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}



symbol_value = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#check which line on the user bets 
def check_winnings( columns, lines, bet, values): 
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] # 1 columns line 1 2 or 3 
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break # if break the statement else does not run 
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) # because is index + 1 -> so we get line 1 2 3 sitead of 012
            
    return winnings, winning_lines # return on which liens they won and total amount they won

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # items gives keys and values  symbol = A, symbol_count = 2
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = [] # finding the column list 
    for col in range(cols):  # for every column do 
        column = []
        current_symbols = all_symbols[:] # copy the list with [:] # current symbols which we can select from 
        for row in range(rows):
            value = random.choice(current_symbols) # picks random value from the list 
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column) 
    
    return columns


def print_slote_machine(columns):  # loop throeugh every raw that we have
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = "|") # 
            else:
                print(column[row], end = "")
        
        print()

def deposit():
    while True: # keep asking the deposit ammoutn untill it is a valid ammount
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("please enter a number")
        else:
            print("Please enter a valid number")
                
    return amount


#Enter the ammount of lines to bet on 
def get_number_of_lines():
    while True: 
        lines = input("Enter the number of lines to bet on (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: #if the value is inbetween 2 values 
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
            
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line ? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number")
                
    return amount



def game(balance):   # returns the net result of one spin
    lines = get_number_of_lines()
    while True:    
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, yout current balance is: ${balance}")
        else:
            break
        
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slote_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines: ", *winning_lines) # for printing every line 
    return winnings - total_bet
    

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        if balance < MIN_BET:
            print("You do not have enough money to play.")
            break

        spin = input("Press enter to spin (q to quit).")
        if spin.lower() == "q":
            break
        balance += game(balance)

    print(f"You left with ${balance}")

main()

