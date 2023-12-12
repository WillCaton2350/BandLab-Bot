from States.data import next_post6,next_post7, next_post8, like_btn10_xpath
from States.data import like_btn6_xpath, like_btn7_xpath, like_btn9_xpath
from States.data import gecko_driver_path, url, user, passwd, login_url
from selenium.common.exceptions import ElementNotInteractableException
from States.data import login_xpath, username_xpath, password_xpath
from States.data import like_btn2_xpath, next_post, like_btn5_xpath
from selenium.webdriver.support import expected_conditions as EC 
from States.data import like_btn4_xpath, next_post4, next_post5
from selenium.webdriver.support.ui import WebDriverWait as WDW 
from States.data import next_post2, like_btn_xpath, next_post3
from States.data import popup_btn, login_btn, like_btn3_xpath
from States.data import next_post9,next_post10, like_btn8_xpath
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from selenium.webdriver.common.by import By
from selenium import webdriver as web
from time import sleep
import os
# Each selenium bot .py file is a microservice

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
# 1 
##########################################################################################################
        try:
            like_button = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, 
                    like_btn_xpath
                )))
            if like_button.is_displayed() and like_button.is_enabled():
                like_button.click()
                print("Post liked")
            else:
                print("Like button not clickable")
        except ElementNotInteractableException as err:
            print(err)

        try:
            next_post_button = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, next_post
                        )))
            if next_post_button.is_displayed() and next_post_button.is_enabled():
                next_post_button.click()
                print("Next post clicked")
                #self.driver.execute_script("window.scrollBy(0, 750);")
                #print('Scrolled down by 750 pixels')
            else:
                print("Next post button not clickable")
        except ElementNotInteractableException as err:
            print(err)
# 2       
##########################################################################################################
        try:
            like_button_two = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, 
                    like_btn2_xpath
                )))
            if like_button_two.is_displayed() and like_button_two.is_enabled():
                like_button_two.click()
                print("Post liked 2")
            else:
                print("Like button not clickable")
        except ElementNotInteractableException as err:
            print(err)
        try:
            next_post_button2 = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, next_post2
                        )))
            if next_post_button2.is_displayed() and next_post_button2.is_enabled():
                next_post_button2.click()
                print("Next post 2 clicked")
                #self.driver.execute_script("window.scrollBy(0, 750);")
                #print('Scrolled down by 750 pixels')
            else:
                print("Next post 2 button not clickable")
        except ElementNotInteractableException as err:
            print(err)
# 3
##########################################################################################################################################
        try:
            like_button_three = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, 
                    like_btn3_xpath
                )))
            if like_button_three.is_displayed() and like_button_three.is_enabled():
                like_button_three.click()
                print("Post liked 3")
            else:
                print("Like button not clickable")
        except ElementNotInteractableException as err:
            print(err)
        try:
            next_post_button3 = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, next_post3
                        )))
            if next_post_button3.is_displayed() and next_post_button3.is_enabled():
                next_post_button3.click()
                print("Next post 3 clicked")
            else:
                print("Next post3 button not clickable")
        except ElementNotInteractableException as err:
            print(err)
# 4
##########################################################################################################################################
        try:
            like_button_four = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, 
                    like_btn4_xpath
                )))
            if like_button_four.is_displayed() and like_button_four.is_enabled():
                like_button_four.click()
                print("Post liked 4")
            else:
                print("Like button not clickable")
        except ElementNotInteractableException as err:
            print(err)
        try:
            next_post_button4 = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, next_post4
                        )))
            if next_post_button4.is_displayed() and next_post_button4.is_enabled():
                next_post_button4.click()
                print("Next post4 clicked")
            else:
                print("Next post 4 button not clickable")
        except ElementNotInteractableException as err:
            print(err)
# 5
##########################################################################################################################################
        try:
            like_button_five = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, 
                    like_btn5_xpath
                )))
            if like_button_five.is_displayed() and like_button_five.is_enabled():
                like_button_five.click()
                print("Post liked 5")
            else:
                print("Like button not clickable")
        except ElementNotInteractableException as err:
            print(err)
        try:
            next_post_button5 = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, next_post5
                        )))
            if next_post_button5.is_displayed() and next_post_button5.is_enabled():
                next_post_button5.click()
                print("Next post 5 clicked")
            else:
                print("Next post 5 button not clickable")
        except ElementNotInteractableException as err:
            print(err)
# 6
##########################################################################################################################################
        try:
            like_button_six = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, 
                    like_btn6_xpath
                )))
            if like_button_six.is_displayed() and like_button_six.is_enabled():
                like_button_six.click()
                print("Post liked 6")
            else:
                print("Like button not clickable")
        except ElementNotInteractableException as err:
            print(err)
        try:
            next_post_button6 = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, next_post6
                        )))
            if next_post_button6.is_displayed() and next_post_button6.is_enabled():
                next_post_button6.click()
                print("Next post 6 clicked")
            else:
                print("Next post 6 button not clickable")
        except ElementNotInteractableException as err:
            print(err)
# 7
##########################################################################################################################################
        try:
            like_button_seven = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, 
                    like_btn7_xpath
                )))
            if like_button_seven.is_displayed() and like_button_seven.is_enabled():
                like_button_seven.click()
                print("Post liked 7")
            else:
                print("Like button not clickable")
        except ElementNotInteractableException as err:
            print(err)
        try:
            next_post_button7 = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, next_post7
                        )))
            if next_post_button7.is_displayed() and next_post_button7.is_enabled():
                next_post_button7.click()
                print("Next post 7 clicked")
            else:
                print("Next post 7 button not clickable")
        except ElementNotInteractableException as err:
            print(err)
# 8
##########################################################################################################################################
        try:
            like_button_eight = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, 
                    like_btn8_xpath
                )))
            if like_button_eight.is_displayed() and like_button_eight.is_enabled():
                like_button_eight.click()
                print("Post liked 8")
            else:
                print("Like button not clickable")
        except ElementNotInteractableException as err:
            print(err)
        try:
            next_post_button8 = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, next_post8
                        )))
            if next_post_button8.is_displayed() and next_post_button8.is_enabled():
                next_post_button8.click()
                print("Next post 8 clicked")
            else:
                print("Next post 8 button not clickable")
        except ElementNotInteractableException as err:
            print(err)
# 9
##########################################################################################################################################
        try:
            like_button_nine = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, 
                    like_btn9_xpath
                )))
            if like_button_nine.is_displayed() and like_button_nine.is_enabled():
                like_button_nine.click()
                print("Post liked 9")
            else:
                print("Like button not clickable")
        except ElementNotInteractableException as err:
            print(err)
        try:
            next_post_button9 = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, next_post9
                        )))
            if next_post_button9.is_displayed() and next_post_button9.is_enabled():
                next_post_button9.click()
                print("Next post 9 clicked")
            else:
                print("Next post 9 button not clickable")
        except ElementNotInteractableException as err:
            print(err)
# 10
##########################################################################################################################################
        try:
            like_button_ten = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, 
                    like_btn10_xpath
                )))
            if like_button_ten.is_displayed() and like_button_ten.is_enabled():
                like_button_ten.click()
                print("Post liked 10")
            else:
                print("Like button not clickable")
        except ElementNotInteractableException as err:
            print(err)
        try:
            next_post_button10 = WDW(
                self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, next_post10
                        )))
            if next_post_button10.is_displayed() and next_post_button10.is_enabled():
                next_post_button10.click()
                print("Next post 10 clicked")
            else:
                print("Next post 10 button not clickable")
        except ElementNotInteractableException as err:
            print(err)

    def close_browser(self):
        self.driver.close()
        # Work on the like feature: 
        # The bot works but not as intended.
        # Needs to like different posts, But Currently likes the same post over and over.
        # Possibly: write a for loop that cycles through the index of a formatted string. EX: f"{1}" - f"{2}" - f"{3}" etc..