import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class BOT_TESTE():
    def __init__(self):
        self.email = input('Digite seu Email: ')
        self.senha = input('Digite sua senha: ')

        self.drive = webdriver.Chrome(executable_path=r'E:\Downloads\chromedriver_win32\chromedriver.exe')


    def acessarPagina(self):
        drive = self.drive
        drive.get("https://www.nike.com.br/?utm_source=GP_search&utm_medium=Cpc&utm_campaign=Nike_Inst&utm_content=Nike&gclid=Cj0KCQiA962BBhCzARIsAIpWEL3niKJrD5Kfqb51xu60Xcgi2VaSyV2iVFfolxeE1Er95-rhRCWV8z0aAkHWEALw_wcB#")
        acesso = drive.find_element_by_xpath('//*[@id="anchor-acessar-unite-oauth2"]').click()
        email = driver.find_element_by_xpath("//*[@type='email']")
        senha = driver.find_element_by_xpath('')
        email.send_keys(self.email)
        senha.send_keys(self.senha)



bot = BOT_TESTE()
bot.acessarPagina()