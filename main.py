# coding:utf-8
import os
import sys
import PIL.Image as PImage
from PIL import ImageFont, ImageDraw
import cv2
import numpy as np
from generator_name import get_name
from generator_sex import get_sex
from generator_nation import get_nation
from generator_date import get_date
from generator_id import get_id
from generator_string import get_string


if getattr(sys, 'frozen', None):
    base_dir = os.path.join(sys._MEIPASS, 'usedres')
else:
    base_dir = os.path.join(os.path.dirname(__file__), 'usedres')
result_dir = os.path.join(os.path.dirname(__file__), 'result')


def changeBackground(img, img_back, zoom_size, center):
    # 缩放
    img = cv2.resize(img, zoom_size)
    rows, cols, channels = img.shape

    # 转换hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 获取mask
    lower_blue = np.array([78, 43, 46])
    upper_blue = np.array([110, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # cv2.imshow('Mask', mask)

    # 腐蚀膨胀
    erode = cv2.erode(mask, None, iterations=1)
    dilate = cv2.dilate(erode, None, iterations=1)

    # 粘贴
    for i in range(rows):
        for j in range(cols):
            if dilate[i, j] == 0:  # 0代表黑色的点
                img_back[center[0] + i, center[1] +
                         j] = img[i, j]  # 此处替换颜色，为BGR通道

    return img_back


def paste(avatar, bg, zoom_size, center):
    avatar = cv2.resize(avatar, zoom_size)
    rows, cols, channels = avatar.shape
    for i in range(rows):
        for j in range(cols):
            bg[center[0] + i, center[1] + j] = avatar[i, j]
    return bg


def getRamdomPic():
    pass


def generator(num):
    global name, sex, nation, year, mon, day, addr, idn, org, life
    ebgvar = True

    # fname = askopenfilename(parent=root, initialdir=os.getcwd(), title=u'选择头像')
    # print fname
    im = PImage.open(os.path.join(base_dir, 'empty.png'))
    # avatar = PImage.open(fname)  # 500x670
    avatar = PImage.open('./resource/head.jpg')

    name_font = ImageFont.truetype(os.path.join(base_dir, 'hei.ttf'), 72)
    other_font = ImageFont.truetype(os.path.join(base_dir, 'hei.ttf'), 60)
    bdate_font = ImageFont.truetype(os.path.join(base_dir, 'fzhei.ttf'), 60)
    id_font = ImageFont.truetype(os.path.join(base_dir, 'ocrb10bt.ttf'), 72)

    draw = ImageDraw.Draw(im)
    draw.text((630, 690), name, fill=(0, 0, 0), font=name_font)
    draw.text((630, 840), sex, fill=(0, 0, 0), font=other_font)
    draw.text((1030, 840), nation, fill=(0, 0, 0), font=other_font)
    draw.text((630, 980), year, fill=(0, 0, 0), font=bdate_font)
    draw.text((950, 980), mon, fill=(0, 0, 0), font=bdate_font)
    draw.text((1150, 980), day, fill=(0, 0, 0), font=bdate_font)
    start = 0
    loc = 1120
    while start + 11 < len(addr):
        draw.text((630, loc), addr[start:start + 11],
                  fill=(0, 0, 0), font=other_font)
        start += 11
        loc += 100
    draw.text((630, loc), addr[start:], fill=(0, 0, 0), font=other_font)
    draw.text((950, 1475), idn, fill=(0, 0, 0), font=id_font)
    draw.text((1050, 2750), org, fill=(0, 0, 0), font=other_font)
    draw.text((1050, 2895), life, fill=(0, 0, 0), font=other_font)

    avatar = cv2.cvtColor(np.asarray(avatar), cv2.COLOR_RGB2BGR)
    im = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2BGR)

    im = changeBackground(avatar, im, (500, 670), (690, 1500))
    im = PImage.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))

    im.save(os.path.join(result_dir, 'color_' + str(num) + '.png'))
    # im.convert('L').save('bw_' + str(num) + '.png')

    print("Idcard #", num, " has successfully been created!")


if __name__ == '__main__':
    global name, sex, nation, year, mon, day, addr, idn, org, life
    for i in range(10000):
        print("========================================================")
        name = get_name()
        print('name: \t\t', name)
        sex = get_sex()
        print('sex: \t\t', sex)
        nation = get_nation()
        print('nation: \t', nation)
        date = get_date()
        year = date.y
        print('year: \t\t', year)
        mon = date.m
        print('month: \t\t', mon)
        day = date.d
        print('day: \t\t', day)
        addr = get_string(15)
        print('address: \t', addr)
        if sex == '男':
            idn = get_id(1)
        elif sex == '女':
            idn = get_id(0)
        print('id: \t\t', idn)
        org = get_string(10)
        print('org: \t\t', org)
        life_ = get_date()
        life = life_.y + life_.m + life_.d
        print('life: \t\t', life)
        generator(i)
