from pyvirtualdisplay import Display
from selenium import webdriver
import urllib
import time
import os

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(CURRENT_PATH, "chromecast-background.jpg")
TEMP_IMAGE_PATH = os.path.join(CURRENT_PATH, "chromecast-background-temp.jpg")
GECKODRIVER_PATH = os.path.join(CURRENT_PATH, "geckodriver")

def init_browser():
    display = Display(visible=0, size=(800, 600))
    display.start()
    return webdriver.Firefox(executable_path=GECKODRIVER_PATH)

def go_to_chromecast_page(browser):
    connected = False
    while(connected == False):
        try:
            browser.get("https://clients3.google.com/cast/chromecast/home")
            connected = True
        except:
            time.sleep(5)


def set_background_img_loop(browser, last_img_uri=""):
    while(True):
        try:
            img_uri = browser.find_element_by_id("picture-background").get_attribute("src")
            if(img_uri != last_img_uri):
                last_img_uri = img_uri
                # save the img
                f = urllib.urlopen(last_img_uri)
                with open(TEMP_IMAGE_PATH, "wb") as imgFile:
                    imgFile.write(f.read())
                # move the file temp_img to img
                os.system("mv %s %s 2>/dev/null" % (TEMP_IMAGE_PATH, IMAGE_PATH))
                # set background desktop
                os.system('gsettings set org.gnome.desktop.background picture-uri "file://'+IMAGE_PATH+'"')
        finally:
            time.sleep(2)

if __name__ == "__main__":
    print("Initializing browser in background...")
    browser = init_browser()
    print("Going to chromecast home page...")
    go_to_chromecast_page(browser)
    print("Start to set chromecast images in background automatically!")
    set_background_img_loop(browser)
