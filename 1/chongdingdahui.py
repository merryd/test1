#coding=utf-8
'''2018.1.27 手写搜题工具python带你开挂玩转冲顶大会'''

import os
import time
from PIL import Image
import pytesseract
import webbrowser

box = (40,400,1380,800)#有效部分

def pull_image():
    os.system('adb shell screencap -p /sdcard/1.png')#手机截图
    os.system('adb pull /sdcard/1.png ./screen/1.png')

def main():
    try:
        #num =1
        #while input('请输入：',):
        while True:
            #img2 = Image.open('./screen/%s.png' % num)
            img2 = Image.open('./screen/1.png')
            img = img2.crop(box)
            #操作ocr
            text = pytesseract.image_to_string(img,lang='chi_sim')
            #print(text)

            text = text.replace(' ','').replace('\n','')
            text = text[text.find('.')+1:text.find('?')]
            #提取的题目交给浏览器 -》找答案
            webbrowser.open('https://www.baidu.com/s?wd='+ text)
            #num += 1
            time.sleep(40)
    except:
        print('未找到')

if __name__ == '__main__':
    pull_image()
    main()
