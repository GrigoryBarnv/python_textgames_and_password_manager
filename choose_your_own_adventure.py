name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input(
    "You are on a dirt road, it has come t the end and you can go left or right. Which way would you liek to go ?")

if answer == "left":
    answer = input("You come to a river, you can walk around or swim across. Type walk around or swim across.")
    
    if answer == "swim":
        print("You swim across and get eaten by an alligator.")
    elif answer == "walk":
        print("You walk for many miles lost water and lost the game.")
    else:
        print("Not a valid option. You lose.")
        
elif answer == "right":
    answer = input("You come to the bridge what you want to do cross it or go back (type cross or back)")
    
    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? Yes or No? ")
        
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You Win! ")
        elif answer == "no":
            print("You ignore the stranger and you lose")
        else:
            print("not a valid option. You lose")
    
    
    else:
        print("Not a valid option. You lose.")
        
    
else:
    print( "Thank you for playing", name)