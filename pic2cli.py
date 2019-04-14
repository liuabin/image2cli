#!pytho3
from cv2 import cv2 as cv
import numpy as np

scale_rate = 5

def colortable(B, G, R):
    if(B == 1):
        if(G == 1):
            if(R == 1):
                return 37
            else:
                return 36
        else:
            if(R == 1):
                return 35
            else:
                return 34
    else:
        if(G == 1):
            if(R == 1):
                return 33
            else:
                return 32
        else:
            if(R == 1):
                return 31
            else:
                return 30


def write_to_file(py_script, string):
    py_script.write("os.system(\"echo -e \'")
    py_script.write(string)
    py_script.write("\'\")")


if __name__ == "__main__":
    img = cv.imread("lena.jpg")
    y = len(img)
    x = len(img[0,:,:])
    # img = cv.resize(img, (128, 128), interpolation=cv.INTER_LANCZOS4)
    py_script = open("test.py", 'w')
    py_script.write("import os\n")

    # img[0,:,:]
    string = ""
    ## two value scale
    # for pixel in img[0,:,:]:
    for j in range(0, x, scale_rate):
        pixel = img[0,j,:]
        color = [0, 0, 0]
        for i in range(3):
            if pixel[i]-128<=0 :
                color[i] = 0
            else:
                color[i] = 1
        color_index = colortable(color[0], color[1], color[2])
        # print(color_index, end="\t")
        string += "\\e[{0};{1};4m  \\e[0m".format(color_index+10, color_index)
    # print(string)

    # write to the .py
    write_to_file(py_script, string)
    write_to_file(py_script, string)

    cv.imshow("test image", img[:,:,:])
    # py_script.write("print(\"\"\" ")
    # py_script.write(str(img[:,:,0]))
    # py_script.write(" \"\"\") ")
    # py_script.write("\n")
    py_script.close()
    cv.waitKey(0)