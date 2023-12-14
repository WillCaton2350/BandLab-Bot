from Bot.service import webDriver
# COMMENT BOT

if __name__ == "__main__":
    func = webDriver()
    func.start_driver()
    func.start_browser()
    func.login()
    #func.popup_interaction()
    func.feed_interaction()
    func.close_browser()