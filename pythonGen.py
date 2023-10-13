import string
import random
import colorama
from colorama import Fore, Style

import os
os.system("cls||clear")

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? : "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    password = "".join(password)
    
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Successfuly Generated Password! : {Fore.LIGHTMAGENTA_EX}{password}{Fore.LIGHTWHITE_EX}{Style.NORMAL}")

while True:
    option = input(f"{Fore.LIGHTCYAN_EX}Do you want to generate a password? (y/n) (quit(q)): {Fore.LIGHTWHITE_EX}")

    if option == "y":
        generate_password()
    elif option == "n":
        print(f"{Fore.RED}Program Ended...{Fore.LIGHTWHITE_EX}")
        quit()
    elif option == "q":
        print(f"{Fore.RED}Program Ended...{Fore.LIGHTWHITE_EX}")
        quit()
    else:
        print(f"{Fore.RED}Invalid Input{Fore.LIGHTWHITE_EX}")