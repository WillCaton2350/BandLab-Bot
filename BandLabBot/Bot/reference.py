from Bot.States.data import gecko_driver_path, url, user, passwd, login_url
from Bot.States.data import login_xpath, username_xpath, password_xpath
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW 
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from Bot.States.data import popup_btn, login_btn
from selenium.webdriver.common.by import By
from Bot.States.data import unfollow_xpath2, unfollow_xpath
from selenium import webdriver as web
from time import sleep
import os
# UNFOLLOW BOT

class Driver:
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
            By.XPATH,
        login_xpath).click()

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
            
    def feed_interaction(self):
        sleep(1)
        WDW(
            self.driver,10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                unfollow_xpath2
            )))
        self.driver.find_element(
            By.XPATH,unfollow_xpath).click()
        print('following_link clicked')
        sleep(1)
        acc_number = 1
        while acc_number <= 7:
            try:
                unfollow_button = WDW(
                    self.driver, 10).until(
                        EC.presence_of_element_located((
                            By.XPATH, 
                f'/html/body/div[6]/aside/div/section/div[2]/div/div[{acc_number}]/user-tile/div/div[2]/div/user-tile-actions/button'
                        )))
                if unfollow_button.is_displayed() and unfollow_button.is_enabled():
                    unfollow_button.click()
                    print(f"Acc {acc_number} unfollowed")
                else:
                    print(f"Acc Btn {acc_number} not clickable")
            except ElementNotInteractableException as err:
                print(err)
            #self.driver.execute_script(
            #"window.scrollBy(0, 60);")
            # Each selenium bot .py file is a like a microservice
            # (But is really a modular monolithic approach to building an application)
            acc_number += 1

    def close_browser(self):
        self.driver.close()