# coding=utf-8
# cv2解决绘制中文乱码

import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont
import  os


#解决CV2不能打印中文的问题
def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, numpy.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)

    font=os.getcwd()+"/font/simsun.ttc";

    # 字体的格式
    fontStyle = ImageFont.truetype(font, textSize, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)
