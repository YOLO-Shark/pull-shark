from time import *
from selenium import webdriver as w # Tự cài thư viện đi nha con đĩ.

videos = open('C:\\path\\to\\link.txt') # Có cái file tên là link.txt đính kèm á, copy đường dẫn paste vô rồi sửa định dạng cho giống vầy nè, nếu đường dẫn có folder tên tiếng việt thì không chạy được đâu bà già m.
list = videos.readlines()

NUM_OF_TAB = 4
NUM_OF_VID = len(list)
LOOP = 30    # 30s một view  ¯\_(ツ)_/¯  chắc vậy  

vid_index = 0
tab_index = 0
count = 1

brow = w.Chrome('C:\\path\\chromedriver.exe') # Tương tự cho bé này luôn, nhỡ không tương thích thì lên search bản nào phù hợp với phiên bản Chrome của mình nha, của mình là 99.
brow.get(list[vid_index])

sleep(1)
play = brow.find_element_by_css_selector('#movie_player > div.ytp-cued-thumbnail-overlay > button')
play.click()

while 1:
    vid_index = (vid_index + 1) % NUM_OF_VID
    tab_index = (tab_index + 1) % NUM_OF_TAB

    if count < NUM_OF_TAB:
        count += 1
        brow.execute_script("window.open('"+list[vid_index].strip()+"')")
    else:
        brow.switch_to.window(brow.window_handles[tab_index])
        sleep(2)
        brow.get(list[vid_index])

    sleep(LOOP)


