from src import Driver

func = Driver()
counter = 10
func.start_driver()
func.start_browser()
func.login()
#func.popup_interaction()
#for i in range(counter):
func.feed_interaction()
func.close_browser()


#from main import webDriver
#
#func = Driver()
#func.start_driver()
#func.start_browser()
#func.login()
#func.popup_interaction()
#func.feed_interaction()
#func.close_browser()