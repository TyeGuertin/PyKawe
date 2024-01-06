import time 
import pygame
pygame.init()

# PyKawe
# pomodoro technique: a schedule for focusing on a task by doing
# 25 minutes of a task then a 5 minute break 
# after 4 intervals of this you take a 15-30 minute break
#
# Thank you for checking out my first python program!
# Kawe means study in Yoruba, a tribute to my study partner, Samuel from Nigeria
#######################################################################################################
# FULL INSTRUCTIONS:
# you must be using windows and have python installed from python.org
# 
#
# go to your desired sound file in file explorer 
# and right click "copy as path" and replace the path in ""

bell = pygame.mixer.Sound(r"C:\Users\WORK\Desktop\PyKawe\BELL.mp3")

# now open windows powershell 
# you must install pygame for the sound function to work.
# type or copy paste this command into powershell 
#
# pip install pygame 
#
# now locate and copy the file path of PyKawe.py
# copy the file path and type python then paste the file path
#
# it will look similar to this:
# python "C:\Users\WORK\Desktop\PyKawe\PyKawe.py"
# that is all, I had a lot of fun making this, thank you for checking it out!

# if you would like to change your work time and break time the values are in seconds
worktime = 1500
breaktime = 300
longbreak = 1800
counter = -1




def interval():
    print("\nWork time has started.")
    bell.play()
    for x in range(worktime, 0, -1):
        print(x)
        time.sleep(1)
      

def takefive():
    print("\nIt's time to take a break!")
    bell.play()
    for x in range(0, breaktime):
        print(x)
        time.sleep(1)


def rest():
    bell.play()
    for x in range(0, longbreak):
        print(x)
        time.sleep(1)


def start():
    bell.play()
    global counter
    counter = counter+1

    another = input("\nYou have done: " + str(counter) + " intervals." " Would you like to start an interval? type anything to continue or q to quit:")
    if another == "q":
        print("\nThanks for using PyKawe!")

        
    else:
        interval()
        if (counter == 4) or (counter == 8) or (counter == 12) or (counter == 16) or (counter == 20):
            bell.play()
            ack = input("\nCongrats! You finished a cycle of four intervals. Please take your extended break. type anything:")
            ack
            
            rest()
        else:
            takefive()
            
        start()
        
    

start()
