from Bot.Feed.Trending.like_trend import web_Driver
# LIKE BOT

if __name__ == "__main__":
    func = web_Driver()
    func.start_driver()
    func.start_browser()
    func.login()
    #func.popup_interaction()
    func.feed_interaction()
    func.close_browser()