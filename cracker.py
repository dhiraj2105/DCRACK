import random
import pyautogui
import string
from datetime import *
from os import system,name

print('''

              _____   _____ _____            _____ _  __
             |  __ \ / ____|  __ \     /\   / ____| |/ /
             | |  | | |    | |__) |   /  \ | |    | ' / 
             | |  | | |    |  _  /   / /\ \| |    |  <  
             | |__| | |____| | \ \  / ____ \ |____| . \ 
             |_____/ \_____|_|  \_\/_/    \_\_____|_|\_\.
                                                            By DHIRAJ

''')

chars=string.printable
chars_list=list(chars)

password=pyautogui.password("Enter a password: ")

def clear():
    if name=='nt':
        _=system('cls')
    else:
        _=system('clear')
clear()

start_time=datetime.now()

guess_password=""

while(guess_password != password):
    guess_password=random.choices(chars_list,k=len(password))

    print("<=============="+str(guess_password)+"==============>")

    if(guess_password == list(password)):
        print("Your password is: " + "".join(guess_password))

        end_time=datetime.now()
        print('Duration: {}'.format(end_time-start_time))

        break