import cv2
import zipfile
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
from skimage.util import random_noise


def take_photo():
    cap1 = cv2.VideoCapture(0)
    i = 0
    while i <= 10:
        ret1, frame1 = cap1.read()
        k = cv2.waitKey(1)
        if k == 27:
            break
        cv2.imwrite('D:\\Queens\\fourth\\cisc499\\facetracking\\final_version\\update\\'+str(i) + '.jpg', frame1)
        i += 1
        cv2.imshow("capture", frame1)
    cap1.release()


def zip_files(files, zip_name):
    os.chdir(r'update')
    zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED )
    for file in files:
        #print('compressing', file)
        zip.write(file)
    zip.close()
    #os.chdir(r'D:\Queens\fourth\cisc499\facetracking\final_version')
    #print('compressing finished')

#files = ['1.jpg','2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg','12.jpg', '13.jpg']#文件的位置，多个文件用“，”隔开
#zip_file = 'pppp.zip'#压缩包名字
#zip_files(files, zip_file)
#take_photo()

def add_noise():
    file_list = os.listdir('grad//')
    for name in file_list:
        os.chdir('grad//' + name)
        # print(os.listdir())
        I = cv2.imread('0.jpg', 1);  # 1/ -1: color mode; 0: gray mode
        # gauss = random_noise(I, mode='gaussian', seed=None, clip=True)
        #sp = random_noise(I, mode='s&p', seed=None, clip=True)
        localvar = random_noise(I, mode='localvar', seed=None, clip=True)

        # plt.subplot(231), plt.imshow(I)
        plt.axis('off')
        plt.imshow(localvar)
        # plt.subplot(233), plt.imshow(sp)
        plt.savefig('8.jpg', bbox_inches='tight')
        os.chdir(r'D:\Queens\fourth\cisc499\facetracking')

#print(os.listdir('grad//'))
#add_noise()