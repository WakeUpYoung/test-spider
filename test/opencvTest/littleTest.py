import time
from aip import AipOcr
import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


if __name__ == '__main__':
    img_path = r'verify_code.png'
    # 灰度读取
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    ret, binary = cv2.threshold(src=img, thresh=0, maxval=255, type=cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    print("threshold value %s" % ret)
    cv2.imwrite('grey.png', binary)
    grey = cv2.imread('grey.png')

    edges = cv2.Canny(grey, 30, 100, apertureSize=3)

    minLineLength = 30  # height/32
    maxLineGap = 5  # height/40
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, minLineLength, maxLineGap)
    line = lines[:, 0, :]
    print(line)

    for x1, y1, x2, y2 in line:
        cv2.line(grey, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow('result', grey)
    k = cv2.waitKey(0)  # waitkey代表读取键盘的输入，括号里的数字代表等待多长时间，单位ms。 0代表一直等待
    if k == 27:  # 键盘上Esc键的键值
        cv2.destroyAllWindows()
