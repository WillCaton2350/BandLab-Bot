from Bot.unfollow import Driver
# UNFOLLOW BOT
# Isn't Not working yet. Work in progress


if __name__ == "__main__":
    counter = 10
    func = Driver()
    for i in range(counter):
        func.start_driver()
        func.start_browser()
        func.login()
        #func.popup_interaction()
        func.feed_interaction()
        counter +=1
    func.close_browser()