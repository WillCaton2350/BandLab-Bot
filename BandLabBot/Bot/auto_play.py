from Bot.States.data import gecko_driver_path, url, user, passwd, login_url
from Bot.States.data import login_xpath, username_xpath, password_xpath
from selenium.common.exceptions import ElementNotInteractableException
from Bot.States.data import popup_btn, login_btn, auto_play_btn_xpath
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW 
from selenium.common.exceptions import NoSuchElementException
from Bot.States.data import user_xpath, search_bar_xpath
from urllib.error import HTTPError as PageNotFoundError
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver as web
from time import sleep
import os
# LIKE BOT

class web_Driver:
    def __init__(self):
        self.driver = None

    def start_driver(self):
        print("Start Browser")
        firefox_options = web.FirefoxOptions()
        firefox_options.add_argument("--mute-audio")
        firefox_options.add_argument("--headless")
        os.environ[
            "webdriver.firefox.driver"
            ] =  gecko_driver_path
        self.driver = web.Firefox(
            options=firefox_options        
        )
        self.driver.maximize_window()

    def start_browser(self):
        self.driver.get(url)
        print("Browser")
        try:
            WDW(self.driver, 
                timeout=10).until(
            EC.url_matches(url))
        except PageNotFoundError as err:
            print(err)

    def login(self):
        try:
            WDW(self.driver, timeout=10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                login_xpath
            )))
        except NoSuchElementException as err:
            print(err)
        self.driver.find_element(
            By.XPATH,login_xpath).click()

        try:
            WDW(self.driver,10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                username_xpath
            )))
        except NoSuchElementException as err:
            print(err)
        self.driver.find_element(
            By.XPATH,
        username_xpath).send_keys(user)
        print("Username typed")
        
        try:
            WDW(self.driver,10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                password_xpath
            )))
        except NoSuchElementException as err:
            print(err)
        self.driver.find_element(
            By.XPATH,
        password_xpath).send_keys(passwd)
        print("Password typed")

        try:
            WDW(self.driver,10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                login_btn
            )))
        except NoSuchElementException as err:
            print(err)
        self.driver.find_element(
            By.XPATH,
        login_btn).click()
        print("Login btn clicked")

    #def checker(self, optional_condition=False):
    #    while True:
    #        try:
    #            self.popup_interaction(optional_condition)
    #        except NoSuchElementException as err:
    #            if optional_condition:
    #                print("Popup not found on the screen:", err)
    #            pass
    #        else:
    #            break
    #    sleep(1)
            

    def popup_interaction(self, optional_condition=True):
        # Still not handling the popup interaction if the 
        # popup element isn't showing on the screen.
        try:
            WDW(
                self.driver, timeout=10).until(
                    EC.url_matches(
                        login_url
                    ))
        except PageNotFoundError as err:
            print(err)
        sleep(1)
        try:
            WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, 
                            popup_btn
                        )))
            if optional_condition:
                self.driver.find_element(
                    By.XPATH, 
                        popup_btn).click()
                print("popup btn clicked")
            else:
                print("Optional condition is False")
                return  
        except NoSuchElementException as err:
            if optional_condition:
                print("Popup not found on the screen:", 
                      err)
                return 
            
    def auto_play(self):
        sleep(1)
        try:
            WDW(
                self.driver,10).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                            search_bar_xpath
                        )))
        except NoSuchElementException as err:
            print(err)
        sleep(1)
        self.driver.find_element(
            By.XPATH,
                search_bar_xpath).send_keys("WillCatonJr")
        print("artist name typed ")
        self.driver.implicitly_wait(1)
        sleep(1)
        self.driver.find_element(
            By.XPATH,search_bar_xpath).send_keys(Keys.ENTER)
        sleep(1)
        try:
            WDW(
                self.driver,10).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                            user_xpath
                    )))
        except ElementNotInteractableException as err:
            print(err)
        sleep(1)
        self.driver.find_element(By.XPATH,user_xpath).click()
        print("user clicked")
        try:
            WDW(
                self.driver,10).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                    auto_play_btn_xpath
                )))
        except NoSuchElementException as err:
            print(err)
        sleep(1)
        self.driver.find_element(By.XPATH,auto_play_btn_xpath).click()
        print('song playing\n')
        sleep(3)

    def close_browser(self):
        print('close browser')
        self.driver.close()