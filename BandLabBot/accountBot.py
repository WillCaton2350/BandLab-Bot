from Bot.accounts import Driver
# FOLLOW BOT

if __name__ == "__main__":
    counter = 10
    func = Driver()
    func.start_driver()
    func.start_browser()
    func.login()
    for i in range(counter):
    #func.popup_interaction()
        func.feed_interaction()
        counter +=1
    func.close_browser()