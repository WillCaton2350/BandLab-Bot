from States.data import gecko_driver_path, url, user, passwd, login_url
from selenium.common.exceptions import ElementNotInteractableException
from States.data import login_xpath, username_xpath, password_xpath
from selenium.webdriver.support import expected_conditions as EC 
from States.data import popup_btn, like_btn_classname, login_btn
from selenium.webdriver.support.ui import WebDriverWait as WDW 
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from States.data import like_btn_css, like_btn_xpath
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver as web
from States.data import comment_classname
from time import sleep
import os

class webDriver:
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
        # Still not handling the popup interaction if the popup element isnt showing on the screen.
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
        # This is the function that needs to be addressed
        self.driver.execute_script(
        "window.scrollBy(0, 10);")
        print('scroll-1')
        # Scroll Down by 10 pixels
        sleep(1)
        try:
            WDW(
                self.driver,10).until(
                    EC.presence_of_element_located((
                        By.CLASS_NAME,
                    comment_classname
                )))
        except ElementNotInteractableException as err:
            print(err)
        sleep(1)
        self.driver.find_element(
            By.CLASS_NAME,
                comment_classname).send_keys("Dope!!")
        sleep(1)
        self.driver.find_element(
            By.CLASS_NAME,
                comment_classname).send_keys(Keys.ENTER)
        sleep(2)
        print("comment sent")
        # This like bot would work if all of the id's were the same or if all of the classnames were the same.
        # Find which locator connects all of the like buttons on the page. (If any)
        # Check if the like button is already clicked and skip that one. Write the exception. 
        # Class_Name should have worked. But it hasn't so far. (Using the beginning of the full class name. Not the full classname)
        sleep(1)
        self.driver.execute_script(
        "window.scrollBy(0, 750);")
        print('scroll-2')
        # Scroll Down by 750 pixels

    def close_browser(self):
        self.driver.close()
        # Work on the like feature: 
        # The bot works but not as intended.
        # Needs to like different posts, But Currently likes the same post over and over.
        # Possibly: write a for loop that cycles through the index of a formatted string. EX: f"{1}" - f"{2}" - f"{3}" etc..