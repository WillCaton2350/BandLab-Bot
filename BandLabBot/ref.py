from Bot.reference import Driver
# UNFOLLOW BOT
# Isn't Not working yet. Work in progress

if __name__ == "__main__":
    func = Driver()
    func.start_driver()
    func.start_browser()
    func.login()
    #func.popup_interaction()
    func.feed_interaction()
    func.close_browser()