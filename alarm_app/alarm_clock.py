from playsound import playsound
import time


## use ANSI characters -> unseen characters that manipulate the terminal 

CLEAR = "\033[2J" # does not work on windows correct use 
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds): # how long to play the alarm
    time_elapsed = 0
    
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1) # wait 1 second untill continue
        time_elapsed += 1
        
        
        #how many seconds and minutes remained
        time_left = seconds - time_elapsed 
        minutes_left = time_left // 60 # 125 // 60 = 2 
        seconds_left =time_left % 60 # 125 % 60 = 5
        
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}", end="\r") # use "\r" intead of CLEAR 
        
    playsound("epic_sound.mp3")
    
minutes = int(input("How many minutes to wait:"))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds    
 
alarm(total_seconds)