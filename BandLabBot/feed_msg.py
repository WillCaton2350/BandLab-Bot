from Bot.Feed.direct_bot import web_driver
# DM BOT

if __name__ == "__main__":
    func = web_driver()
    func.start_driver()
    func.start_browser()
    func.login()
    #func.popup_interaction()
    func.feed_interaction()
    func.close_browser()