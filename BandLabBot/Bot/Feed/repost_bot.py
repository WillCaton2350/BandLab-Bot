from Bot.States.data import gecko_driver_path, url, user, passwd, login_url
from Bot.States.data import login_xpath, username_xpath, password_xpath
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW 
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from Bot.States.data import repost_textarea_xpath
from Bot.States.data import popup_btn, login_btn
from Bot.States.data import post_repost_xpath
from selenium.webdriver.common.by import By
from Bot.States.data import repost3_xpath
from Bot.States.data import foryou_xpath
from selenium import webdriver as web
from time import sleep
import os
# REPOST BOT

class web_driver:
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
        # This repost bot only reposts the top post
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
        try:
            WDW(
                self.driver,10).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                            foryou_xpath
                        )))
        except NoSuchElementException as err:
            print(err)
        self.driver.find_element(
            By.XPATH,
                foryou_xpath).click()
        self.driver.implicitly_wait(1)
        sleep(1)
        post_number = 1
        while post_number <= 1:
            try:
                repost_btn = WDW(
                    self.driver, 10).until(
                        EC.presence_of_element_located((
                            By.XPATH, 
        f'/html/body/main/div/section/div[2]/div[2]/div[3]/div/div[{post_number}]/post-card/div/post-tile-social/div/div[1]/div'
                                       
                        )))
                if repost_btn.is_displayed() and repost_btn.is_enabled():
                    repost_btn.click()
                    self.driver.implicitly_wait(1)
                    sleep(1)
                    self.driver.find_element(
                            By.XPATH, repost3_xpath).click()
                    self.driver.implicitly_wait(1)
                    sleep(1)
                    self.driver.find_element(
                        By.XPATH,
                            repost_textarea_xpath
                        ).send_keys("Reposted!!!")
                    self.driver.implicitly_wait(1)
                    sleep(1)
                    self.driver.execute_script(
                        "window.scrollBy(0, 20);")
                    self.driver.find_element(
                        By.XPATH,
                            post_repost_xpath).click()
                    print(f"Post {post_number} reposted")
                else:
                    print(f"repost button for post {post_number} not clickable")
            except ElementNotInteractableException as err:
                print(err)
            try:
                next_post_button = WDW(
                    self.driver, 10).until(
                        EC.presence_of_element_located((
                            By.XPATH, 
                f'/html/body/main/div/section/div[2]/div[2]/div[3]/div/div[{post_number}]/post-card/div')))
                self.driver.execute_script(
                    "arguments[0].scrollIntoView();", next_post_button)
                if self.driver.find_element(By.XPATH, next_post_button):
                    print(f"Next post {post_number} clicked")
                else:
                    print(f"Next post {post_number} button not clickable")
            except ElementNotInteractableException as err:
                print(err)

    def close_browser(self):
        self.driver.close()