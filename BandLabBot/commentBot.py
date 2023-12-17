from Bot.comment import webDriver
# COMMENT BOT

if __name__ == "__main__":
    counter = 10
    func = webDriver()
    func.start_driver()
    func.start_browser()
    func.login()
    #func.popup_interaction()
    func.feed_interaction()
    func.close_browser()