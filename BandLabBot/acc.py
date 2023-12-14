from Bot.accounts import Driver
# FOLLOW BOT

if __name__ == "__main__":
    func = Driver()
    func.start_driver()
    func.start_browser()
    func.login()
    #func.popup_interaction()
    func.feed_interaction()
    func.close_browser()