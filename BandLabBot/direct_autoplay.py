from Bot.autoplay_direct import web_Driver

if __name__ == "__main__":
    counter = 100
    func = web_Driver()
    for i in range(counter):
        func.start_driver()
        func.start_browser()
        func.popup_interaction()
        func.auto_play()
        counter +=1
    func.close_browser()