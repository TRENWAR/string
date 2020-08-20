# import module
import os
from time import sleep


# it's just color
white  = '\033[37m'
cyan   = '\033[36m'
yellow = '\033[93m'
green  = '\033[92m'
pink   = '\033[95m'
red    = '\033[91m'

    
    
    
    
# def mainMenu
def mainMenu():
    os.system("clear")
    print(10*"="+"Welcome"+10*"=")
    print("Welcome to this tools\r\nThis tools can manipulate string (using Python)")
    
    
    
    
# def chooseColor
def chooseColor():
    os.system("clear")
    print(10*"="+"Welcome"+10*"=")
    print("Before we start, please select the color first")
    print("1.Original (white (cuz you're original & simple boy)\r\n2.Red (cuz you like Red..??)\r\n3.Yellow (cuz idk why)\r\n4.Pink (cuz u watched Barbie or something)\r\n5.Cyan (cuz that a nice color???)\r\n6.Green (cuz u want to look like Hacker (fck)")
    user = input("~~> ")
    
    
    if user == "1":
        print(white+"Nice, this is what i've been waiting for 20 years...Nice :)")
        sleep(1.7)
        mainMenu()
        
        
    elif user == "2":
        print(red+"Nice, i mean pretty nice :)")
        sleep(0.9)
        mainMenu()
        
        
    elif user == "3":
        print(yellow+"Oke")
        sleep(0.4)
        mainMenu()
        
        
        
    elif user == "4":
        print(pink+"Nice fcking choise :D")
        sleep(0.8)
        mainMenu()
        
        
    elif user == "5":
        print(cyan+"Cool mode on i mean Cyan")
        sleep(0.6)
        mainMenu()
        
        
    elif user == "6":
        print(green+"if u like green & u choose this Np\r\nbut if u wan't to look like Hacker this is not hacking tools Wtf\r\nbut Np u can use this tools Xd")
        sleep(0.4)
        
        user = input("So do u wan't to use my tool Y/n: ")
        if user == "Y":
            print("Oke")
            sleep(0.4)
        else:
            print("Oke")
            os.system("exit")
    
    else:
        print("Im serious")
        
        
        

# def mainMenu
def mainMenu():
    os.system("clear")
    print(8*"="+"Welcome"+8*"=")
    print("Welcome to this tools\r\nThis tools can manipulate string (using Python)")




chooseColor()
# Beta version 
