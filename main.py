import time
from re import T

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

import random


class Boot:
    def __init__(self):
        options = Options()
        # options.add_argument("--user-data-dir=/home/renan/.config/google-chrome")

        # options.add_argument("--profile-directory=/home/renan/.config/google-chrome")
        # options.add_argument("headless")
        print(options.arguments)

        self.browser = webdriver.Chrome(
            options=options, executable_path='./chromedriver')
        self.browser.maximize_window()

    def login(self):
        browser = self.browser
        browser.get("https://web.whatsapp.com")
        print("Escanei o QR code")
        input()
        print("Logado")

    def send_message(self, numero, message):
        browser = self.browser
        # browser.get("https://api.whatsapp.com/send?={}&text={}".format(numero, message))
        # Alert(browser).accept()
        inp_xpath_search = "//input[@title='Search or start new chat']"
        input_box_search = WebDriverWait(browser, 50).until(
            lambda driver: browser.find_element(By.XPATH, inp_xpath_search))
        input_box_search.click()
        time.sleep(2)
        input_box_search.send_keys(browser)
        time.sleep(2)
        selected_contact = browser.find_element(By.XPATH, "//span[@title=' darling ']")
        selected_contact.click()
        inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
        input_box = browser.find_element(By.XPATH, inp_xpath)
        time.sleep(2)
        input_box.send_keys(browser + Keys.ENTER)
        time.sleep(2)


numero = '553189791428'
message = 'Mensagem enviada'

executar = Boot()
executar.login()
executar.send_message(numero, message)
