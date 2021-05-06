
import time

from selenium import webdriver

try:
    fireFoxOptions = webdriver.FirefoxOptions()
    
    fireFoxOptions.set_headless()
    fireFoxOptions.set_preference("media.navigator.streams.fake", True)
    
    fireFoxOptions.set_preference("permissions.default.microphone", False)
    fireFoxOptions.set_preference("permissions.default.camera", True)
    

    brower = webdriver.Firefox(executable_path='./geckodriver',firefox_options=fireFoxOptions)

    brower.get('https://meet.guifi.net/prova_selenium')
    #print(brower.page_source)
    time.sleep(120)
finally:
    try:
        brower.close()
    except:
        pass
