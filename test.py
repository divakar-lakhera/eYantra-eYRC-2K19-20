import cv2 as cv
import numpy as np
from numpy.fft import *
# import cv2.aruco as aruco

def wiener_filter(img, kernel, K):
	kernel /= np.sum(kernel)
	dummy = np.copy(img)
	dummy = fft2(dummy)
	kernel = fft2(kernel, s = img.shape)
	kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + K)
	dummy = dummy * kernel
	dummy = np.abs(ifft2(dummy))
	return dummy

vid=cv.VideoCapture("../Videos/aruco_bot.mp4")
fps = vid.get(cv.CAP_PROP_FPS)
# 6th sec = 5*fps + 1
itrs = 1 * int(fps) + 1
frame = None
for i in range(itrs):
    _, frame = vid.read()
crop_img = frame[0:725, 0:1282]
kernel_size=20;
kernel_v = np.zeros((kernel_size, kernel_size))
kernel_v[:,int((kernel_size - 2)/2)] =(-1)* np.ones(kernel_size)
kernel_v[:,int((kernel_size)/2)] = (-1)*np.ones(kernel_size)

print(kernel_v)
cv.imshow("kernl",wiener_filter(cv.cvtColor(crop_img,cv.COLOR_BGR2GRAY),kernel_v,150))
cv.waitKey()
#cv.imwrite('tempDump.jpg',)