from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW 
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from Bot.States.data import main_btn_ap
from Bot.States.data import gecko_driver_path
from selenium.webdriver.common.by import By
from Bot.States.data import main_url, popup_btn
from selenium import webdriver as web
from time import sleep
import os
# autoplay2 BOT

class web_Driver:
    def __init__(self):
        self.driver = None

    def start_driver(self):
        print("Start Browser")
        firefox_options = web.FirefoxOptions()
        os.environ[
            "webdriver.firefox.driver"
            ] =  gecko_driver_path
        self.driver = web.Firefox(
            options=firefox_options        
        )
        self.driver.maximize_window()

    def start_browser(self):
        self.driver.get(main_url)
        print("Browser")
        try:
            WDW(self.driver, 
                timeout=10).until(
            EC.url_matches(main_url))
        except PageNotFoundError as err:
            print(err)
    
    def popup_interaction(self, optional_condition=True):
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
                self.driver,5).until(
                    EC.presence_of_element_located((
                        By.XPATH,main_btn_ap
                )))
        except NoSuchElementException as err:
            print(err)
        
        self.driver.find_element(
            By.XPATH,main_btn_ap).click()
        print('song playing\n')
        sleep(1)

    def close_browser(self):
        print('close browser')
        self.driver.close()
