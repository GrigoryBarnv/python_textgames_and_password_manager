print("Welcome to my computer quiz game!")

playing = input("Do you want to play?") # start typing in smth in a console 

text = "Tim is great!"

print(text.lower())

score = 0

if playing != "yes":
    quit() # if user does not want to play, just quit the programm

print("Okey, let's play!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
   

answer = input("What does RAM stand for? ")
if answer.lower() == "random acces memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic prozessing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You got " + str(score)+ " questions correct!")

print("You got " + str((score / 4) * 100) + "%" " questions correct!")



    
 