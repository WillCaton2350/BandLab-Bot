from Bot.States.data import gecko_driver_path, url, user, passwd, login_url
from Bot.States.data import login_xpath, username_xpath, password_xpath
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW 
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from Bot.States.data import popup_btn, login_btn
from selenium.webdriver.common.by import By
from selenium import webdriver as web
from time import sleep
import os
# LIKE BOT

class Driver:
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
        
        post_number = 1
        while post_number <= 10:
            try:
                like_button = WDW(
                    self.driver, 10).until(
                        EC.presence_of_element_located((
                            By.XPATH, 
                f"/html/body/main/div/section/div[2]/div[2]/div[3]/div/div[{post_number}]/post-card/div/post-tile-social/div/div[1]/span/like"
                        )))
                if like_button.is_displayed() and like_button.is_enabled():
                    like_button.click()
                    print(f"Post {post_number} liked")
                else:
                    print(f"Like button for post {post_number} not clickable")
            except ElementNotInteractableException as err:
                print(err)
            try:
                next_post_button = WDW(
                    self.driver, 10).until(
                        EC.presence_of_element_located((
                            By.XPATH, 
                f'/html/body/main/div/section/div[2]/div[2]/div[3]/div/div[{post_number}]/post-card/div'
                        )))
                if next_post_button.is_displayed() and next_post_button.is_enabled():
                    next_post_button.click()
                    print(f"Next post {post_number}")
                else:
                    print(f"Next post {post_number} button not clickable")
            except ElementNotInteractableException as err:
                print(err)
            # Each selenium bot .py file is a like a microservice
            # (But is really a modular monolithic approach to building an application)
            post_number += 1

    def close_browser(self):
        self.driver.close()