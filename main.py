import time
from re import T

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

import random


class Boot:
    def __init__(self, username, password):

        self.username = username
        self.password = password
        options = Options()
        # options.add_argument("headless")
        self.browser = webdriver.Chrome(
            options=options, executable_path='./chromedriver')
        self.browser.maximize_window()

    def login(self):
        browser = self.browser
        browser.get("https://www.instagram.com/")
        try:
            time.sleep(5)
            login_button = browser.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']"
            )
            login_button.click()
        except:
            print('já estamos na página de login')
            pass
        user_element = browser.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        time.sleep(random.randint(4, 6))
        user_element.send_keys(self.username)
        time.sleep(random.randint(4, 6))
        password_element = browser.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(random.randint(4, 6))
        password_element.send_keys(Keys.RETURN)
        try:
            time.sleep(random.randint(4, 6))
            ativar_notificacao = browser.find_element(By.XPATH,
                                                      "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")
            ativar_notificacao.click()
            time.sleep(5)
        except Exception as e:
            print(e)
            pass

    def curtir_fotos_com_a_hastag(self, hashtag, seguir_hastag, paginas, curtiu, seguiu):
        browser = self.browser
        browser.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        # if seguir_hastag:
        #     try:
        #         browser.find_element(By.PARTIAL_LINK_TEXT, "Seguir").click()
        #     except Exception as e:
        #         print(e)
        #         time.sleep(5)

        for i in range(
                1, paginas
        ):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
            browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = browser.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        testes = [
            href
            for href in pic_hrefs
            if hashtag in href and href.index("https://www.instagram.com/p") != -1
        ]

        for pic_href in pic_hrefs:
            try:
                pic_href.index("https://www.instagram.com/p")
            except ValueError as err:
                print("pulando link inválido")
                continue
            browser.get(pic_href)
            browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(10, 12))
                if curtiu:
                    curtir = browser.find_element(By.XPATH,
                                                  "//span[@class='_aamw']//button")
                    curtir.click()
                if seguiu:
                    browser.find_element(By.XPATH, "//div[@class='_aacl _aaco _aacw _aad6 _aade']").click()

                time.sleep(random.randint(25, 27))
            except Exception as e:
                print(e)
                time.sleep(5)


def defini_hastag():
    hastag = input(' Deseja curtir ou seguir alguma hastg especifica ? 1- sim 2- Não\n')
    if hastag == '1':

        while True:
            opcao = input("Qual hastag deseja ? \n")
            if not opcao:
                print("Escreva alguma coisa\n")
            else:
                break
                
        executar.curtir_fotos_com_a_hastag(opcao, 50, True, True, True)
    elif hastag == '2':
        print(hastag)
    else:
        print("opção invalidas, tente novamente\n")
        defini_hastag()

nome = input(
    'Informe os dados para login: \n')

senha = input('Informe a senha de login: \n')


executar = Boot(nome, senha)
executar.login()
defini_hastag()


