from Bot.Feed.Trending.comment_trend import webDriver
# LIKE BOT

if __name__ == "__main__":
    func = webDriver()
    func.start_driver()
    func.start_browser()
    func.login()
    func.popup_interaction()
    func.feed_interaction()
    func.close_browser()