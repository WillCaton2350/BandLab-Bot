from main import webDriver

func = webDriver()
counter = 10
func.start_driver()
func.start_browser()
func.login()
func.popup_interaction()
for i in range(counter):
    func.feed_interaction()
    counter+=1
func.close_browser()