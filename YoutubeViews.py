from time import *
from selenium import webdriver as w

videos = open('D:\\D - Files\\PyC++\\Python\\Tools\\link.txt')
list = videos.readlines()

NUM_OF_TAB = 4
NUM_OF_VID = len(list)
LOOP = 30

vid_index = 0
tab_index = 0
count = 1

browser = w.Chrome('D:\\D - Files\\PyC++\\Python\\Tools\\chromedriver.exe')
browser.get(list[vid_index])

sleep(1)
play = browser.find_element_by_css_selector('#movie_player > div.ytp-cued-thumbnail-overlay > button')
play.click()

while 1:
    vid_index = (vid_index + 1) % NUM_OF_VID
    tab_index = (tab_index + 1) % NUM_OF_TAB

    if count < NUM_OF_TAB:
        count += 1
        browser.execute_script("window.open('"+list[vid_index].strip()+"')")
    else:
        browser.switch_to.window(browser.window_handles[tab_index])
        sleep(2)
        browser.get(list[vid_index])

    sleep(LOOP)


