import pyautogui
import time
from PIL import Image

pyautogui.PAUSE=2.0



#解决分辨率问题
def resolution_ratio(img_url):
    #这里假设的是
    img=Image.open(img_url)
    program_screen_size=(2560,1600)   #这里得分辨率是原始编写代码的设备进行截图的屏幕的分辨率

    current_screen_size=pyautogui.size()

    screen_dpi_width=current_screen_size[0]/program_screen_size[0]
    screen_dpi_height=current_screen_size[1]/program_screen_size[1]

    out_img=img.resize((   int(img.size[0]*screen_dpi_width),   int(img.size[1]*screen_dpi_height)  ))
    return out_img

def fun_loop( fun,timeout=10,correct="",error=""):
    # find_bool  表示是否找到
    find_bool=False
    start_time=time.time()
    while time.time()-start_time<timeout:
        find_bool=fun()
        if find_bool:
            print(correct)
            return None
        print("\b"*4,end="")
        print('try ',end="")

    print(error)


#Start qidian
def start_qidian():
    try:
        location=pyautogui.locateOnScreen(resolution_ratio("./images/qidian/01_qidian.png"),grayscale=False,confidence=0.9)
        pyautogui.click(location,button='left')
        return(bool(location))
    except pyautogui.ImageNotFoundException:
        return False
        # print("Image not find")

#click_button_'me'
def click_button_me():
    try:
        location=pyautogui.locateOnScreen(resolution_ratio("./images/qidian/02_me.png"),grayscale=False,confidence=0.9)
        pyautogui.click(location,button="left")
        return(bool(location))
    except pyautogui.ImageNotFoundException:
        return False

#click welfare
def click_welfare():
    try:
        location=pyautogui.locateOnScreen(resolution_ratio("./images/qidian/03_welfare.png"),grayscale=True,confidence=0.8)
        pyautogui.click(location,button="left")
        return(bool(location))
    except pyautogui.ImageNotFoundException:
        return False

#click watch video
def click_video():
    try:
        location=pyautogui.locateOnScreen(resolution_ratio("./images/qidian/04_watch_video.png"),grayscale=True,confidence=0.8)
        pyautogui.click(location,button="left")
        return(bool(location))
    except pyautogui.ImageNotFoundException:
        return False

#click close0
def click_close_0():
    try:
        location=pyautogui.locateOnScreen(resolution_ratio("./images/qidian/06_0_close.png"),grayscale=True,confidence=0.8)
        pyautogui.click(location,button="left")
        return(bool(location))
    except pyautogui.ImageNotFoundException:
        return False

#click close1
def click_close_1():
    try:
        location=pyautogui.locateOnScreen(resolution_ratio("./images/qidian/06_1_close.png"),grayscale=True,confidence=0.8)
        pyautogui.click(location,button="left")
        return(bool(location))
    except pyautogui.ImageNotFoundException:
        return False

def click_haven_known():
    try:
        location=pyautogui.locateOnScreen(resolution_ratio("./images/qidian/07_haven_known.png"),grayscale=True,confidence=0.8)
        pyautogui.click(location,button="left")
        return(bool(location))
    except pyautogui.ImageNotFoundException:
        return False

def specific_fun_loop( fun,timeout=10,correct="",error=""):
    # find_bool  表示是否找到
    find_bool=False
    start_time=time.time()
    while time.time()-start_time<timeout:
        find_bool=fun()
        if find_bool:
            print("done")
            find_bool=True
            print(correct)
            return find_bool
        print("\b"*4,end="")
        print('try ',end="")

    print(error)
    return find_bool


#将调用函数集合在一个函数里面


def main_fun():
    fun_loop(start_qidian,timeout=10,correct="qidian found!",error="qidian not find")
    fun_loop(click_button_me,timeout=15,correct="button_me found!",error="button_me not find")
    fun_loop(click_welfare,timeout=5,correct="button_welfare found!",error="button_welfare not find")

    for i in range(0,8):
        find_bool=False
        fun_loop(click_video,timeout=5,correct="watch_video found!",error="watch_video not find")
        find_bool=specific_fun_loop(click_close_1,timeout=18,correct="close_1 found!",error="close_1 not find")
        fun_loop(click_haven_known,timeout=5,correct="haven_known_button found",error="haven_known_button not found")
        if find_bool:
            continue
        find_bool=specific_fun_loop(click_close_0,timeout=7,correct="close_0 found!",error="close_0 not find")
        fun_loop(click_haven_known,timeout=5,correct="haven_known_button found",error="haven_known_button not found")
        if find_bool:
            continue
        find_bool=specific_fun_loop(click_close_1,timeout=10,correct="close_1 found!",error="close_1 not find")
        fun_loop(click_haven_known,timeout=5,correct="haven_known_button found",error="haven_known_button not found")
        if find_bool:
            continue

if __name__=='__main__':
    main_fun()