from Bot.auto_play import web_Driver
from time import sleep
# AUTOPLAY BOT

if __name__ == "__main__":
    counter = 100
    func = web_Driver()
    for i in range(counter):
        sleep(1)
        func.start_driver()
        func.start_browser()
        func.login()
        #func.checker()
       # func.popup_interaction()
        func.auto_play()
        counter+=1
    func.close_browser()