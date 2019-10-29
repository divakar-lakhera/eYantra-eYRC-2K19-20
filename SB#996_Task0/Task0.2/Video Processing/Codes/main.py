import cv2 as cv
import numpy as np

def _doTask1(dev):
    fps = dev.get(cv.CAP_PROP_FPS)

    itrs=5*int(fps) +1
    frame=None
    for i in range(itrs):
        _ , frame = dev.read()
    cv.imwrite('../Generated/frame_as_6.jpg', frame)

def _doTask2():
    img = cv.imread('../Generated/frame_as_6.jpg')

    img[:, :, 0:2] = [0]
    cv.imwrite('../Generated/frame_as_6_red.jpg', img)




if __name__ == "__main__" :


    cDev = cv.VideoCapture('../Videos/RoseBloom.mp4')
    _doTask1(cDev)
    _doTask2()
    exit();

