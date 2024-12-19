from adbutils import AdbClient
import adbutils,time,cv2
from PIL import Image

client=AdbClient(host="127.0.0.1",port=5037)

#MUMU模拟器默认端口16384
client.connect(addr="127.0.0.1:16384")


devices=client.device_list()

device1=devices[0]


def image_return():
    '''
    返回设备截图
    '''
    screenshot=device1.screenshot()
    screenshot.save("./temp/temp_image.png")
    return screenshot

def adb_click(location):
    '''
    点击设备
    x,y 是要点击的坐标，一般由图像识别给出
    '''
    #下面这些注释掉的内容是我用来验证点击的坐标的正确性的
    # print(location)
    device1.click(int(location[0]+location[2]/2), int(location[1]+location[3]/2))
    # print(f"click{ int(location[0]+location[2]/2), int(location[1]+location[3]/2)}")
    # img=cv2.imread("./temp/temp_image.png")
    # img2=cv2.rectangle(img=img,pt1=(location[0],location[1]),pt2=(int(location[0]+location[2]/2), int(location[1]+location[3]/2)),color=(0,255,0),thickness=3)
    # print("img2 shape:")
    # print(img2.shape)
    # pil_img=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    # img2_pil=Image.fromarray(pil_img)
    # img2_pil.show()
    # cv2.imshow("img2",img2)
    # cv2.waitKey(0)=="Q"
