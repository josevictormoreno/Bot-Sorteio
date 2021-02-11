import time
from random import randint

def input_username():
    print('\033[1;31m *************************************************************')
    print('\033[1;31m *                    BOT SORTEIO INSTA                      *')
    print('\033[1;31m *************************************************************')
    print('\033[m \n\nObs: O NOME DE USUÁRIO E SENHA SÃO CRIPTOGRAFADOS!')
    print('Exemplo -> senha: botsorteio')
    print("Criptografando...")
    list_alf = ["akdjfuvifi","hudu7eojgb","c@oodjodd","a#jsjdodjo","ejidoso112","jdj&dddpf"]
    time.sleep(2)
    print("...")
    time.sleep(1)
    print("senha criptografada:\n")
    crip = list_alf[randint(0,len(list_alf))]
    print(crip)
    username = input("**** Username: ")
    return username

def input_password():
    password = input("**** Password: ")
    time.sleep(1)
    print('O bot_sorteio esta sendo inciado...')
    return password