import os
import shutil
import sys

import sounddevice as sd
from playsound import *
from scipy.io.wavfile import write

soundslist = []


def main():  # Main function
    while True: #Forever cycle
        try: #Try
            print("For player write 0 for add new song to list write 1 , for record new sound 2 and for exit write 3") #Print
            userinput = int(input()) #Save user answer to variable userinput
            if userinput == 0: #If user input is 0:
                player() #Call player unction
            elif userinput == 1: #If user input is 1:
                new_song() #Call new_song function

            elif userinput == 2: #If user input is 2:
                record() #Call record function

            elif userinput == 3: #If user input is 3:
                sys.exit() #Exit code
            else: #Else
                print("Please Enter valid number") #Print
        except:
            pass


def player(): #Function player
    print("player")
    print(soundslist) #Print list of your saved sounds

    userinput = int(input("Enter song number please"))
    try:
        playsound(soundslist[userinput]) #Playsound from userinput
    except:
        playsound(userinput)
    finally:
        sys.exit("This song does not exist") #If sound not exist exit code


def new_song(): #Adding new sound to list
    print("For add new song write path to new song")
    path = input() #Variable path is user input
    soundslist.append(path)#Adding path to soundlins
    print(soundslist)#Print all saved sounds


def record():
    fs = 44100  # Sample rate
    seconds = int(input("Long of your sound"))  # Duration of recording
    name = input("What is the name of your sound")  # Set name of your sound
    fullname = name + '.wav'  # add .wav to name of your file
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)  # Start recording sound
    sd.wait()  # Waiting
    write(fullname, fs, myrecording)  # Saving your file
    shutil.copy(fullname, 'Sounds', follow_symlinks=True)  # copiing yout file to folder Sounds
    os.remove(fullname)


if __name__ == '__main__':
    try:
        if os.path.isdir('./Sounds'):  # If folder Sounds exist
            pass
        else:  # If not
            os.makedirs('Sounds')  # Make folder sounds
    except:
        pass

    main()  # Call main function
