#!python3
#########################
# A little python Script displaying images in pure command Terminal.
# Generate .sh file 
#########################
import numpy as np
from cv2 import cv2 as cv
import sys
# import random


def colortable(opencv_color:list):
    B = opencv_color[0]>>7
    G = opencv_color[1]>>7
    R = opencv_color[2]>>7
    if(B>0):
        B = 1
    if(G>0):
        G = 1
    if(R>0):
        R = 1
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

def wirte_to_file (all_cmd:str):
    sh_file = open(filename+".sh", 'w')
    string = "#!/bin/bash\n"
    string += all_cmd
    sh_file.write(string)
    
def gen_a_cmd_list(color_list:list):
    cmd_list = r"echo -e '"
    for color in color_list:
        tempi = int(color)
        if tempi < 30 or tempi > 37:
            tempi = 30
            print("Fuck")
        cmd_list += "\\e[{0};{1};4m".format(tempi+10, tempi)
        cmd_list += "  "
        cmd_list += "\\e[0m"
    cmd_list += "'\n"
    return cmd_list

def gen_cmd_list(color_matrix):
    all_cmd = ""
    for line in color_matrix:
        all_cmd += gen_a_cmd_list(line)
    # all_cmd += gen_a_cmd_list(range(30,38))
    # all_cmd += gen_a_cmd_list(range(31,37))
    wirte_to_file(all_cmd)

def conv_color(img, x:int, y:int):
    color_matrix = np.zeros((y,x), int)
    # Maybe Greater
    for ty in range(y):
        for tx in range(x):
            # color_matrix[ty,tx] = random.randint(30,37)
            color_matrix[ty, tx] = colortable(img[ty, tx, :])
    gen_cmd_list(color_matrix)

def image_read(filename:str):
    ter_size = (64, 64)
    img = cv.imread(filename) # (200,200)
    if(img.size):
        pass
    else:
        exit(-1)
    y = len(img)
    x = len(img[0])
    if(x<ter_size[1] and y<ter_size[0]):
        ter_size = (y, x)
    else:
        while(True):
            y >>= 1
            x >>= 1
            if(x < ter_size[1] and y < ter_size[0]):
                break
        ter_size = (x, y)
        # print(ter_size)
        img = cv.resize(img, ter_size, interpolation=cv.INTER_LANCZOS4)
        cv.imwrite("Z23test.jpg", img)
        # cv.imshow("test", img)
        # cv.waitKey(0)
    conv_color(img, ter_size[0], ter_size[1])

def main():
    global filename
    if (len(sys.argv)>1):
        filename = sys.argv[1]
    else:
        filename = "lena.jpg"
        # filename = "opencv-logo.png"
    image_read(filename)   

if __name__ == "__main__":
    # wirte_to_file(cmd + "\n")
    # gen_a_cmd_list(range(30,38))
    # gen_cmd_list([[31,32,33], [34,35,36]])
    main()

