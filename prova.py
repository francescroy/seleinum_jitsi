#!/usr/bin/env python3


from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time


display = Display(visible=0, size=(1366, 768))
display.start()


opt = Options()

opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })


#opt.add_argument('headless')

opt.add_argument('use-fake-ui-for-media-stream')
opt.add_argument('disable-web-security')
opt.add_argument('use-fake-device-for-media-stream')
opt.add_argument('use-file-for-fake-video-capture=video_fake.y4m')
opt.add_argument('use-file-for-fake-audio-capture=audio_fake.wav')
opt.add_argument('allow-file-access')

driver = webdriver.Chrome(options=opt,executable_path="./chromedriver")
driver.get("https://upcjitsi.exo.cat/francesc-pedro")
#print(driver.title)



time.sleep(120)


# quit browser
driver.quit()

# quit Xvfb display
display.stop()
