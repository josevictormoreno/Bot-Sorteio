import time
from random import randint

def input_username():
    print('\033[1;31m *****************************************************')
    print('\033[1;31m *                    BOT INSTA                      *')
    print('\033[1;31m *****************************************************')
    username = input("**** Username: ")
    return username

def input_password():
    password = input("**** Password: ")
    time.sleep(1)
    print('Starting...')
    return password
