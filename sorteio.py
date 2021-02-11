import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import botInput as inpt

class Instagram_bot:
    def __init__(self,username, password, list_user):
        self.username = username
        self.password = password
        self.list_user = list_user
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/?hl=pt-br")
        time.sleep(3)
        loginButton = driver.find_element_by_xpath("//input[@name='username']")
        loginButton.click()
        loginButton.clear()
        loginButton.send_keys(self.username)
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(8)
        self.comentar()

    def comentar(self):
        driver = self.driver
        driver.get('https://www.instagram.com/p/CLFrxGsFfsX/')
        time.sleep(5)
        
        while True:
            driver.find_element_by_class_name("Ypffh").click()
            campo_comentario = driver.find_element_by_class_name("Ypffh")
            campo_comentario.send_keys(self.list_user[randint(0,2)])
            time.sleep(5)
            campo_comentario.send_keys(Keys.SPACE)
            time.sleep(5)
            campo_comentario.send_keys(Keys.ENTER)
            time.sleep(30)

'''
USUARIOS 
@brunofigfre @eliseunetoo
@lucaszeviani @raphaelcogo
@thiagotissei @eduardolachimia
@henriqueletrari @nobile.caio
@_tavinpaviani @jgvmartini
'''

list_user = ["@albuquerquethiago @vitorlucenaaa", "@thiagotissei @lucaszeviani", "@raphaelcogo @brunofigfre"]
username = inpt.input_username()
password = inpt.input_password()

bot_sorteio = Instagram_bot(username,password, list_user)
bot_sorteio.login()