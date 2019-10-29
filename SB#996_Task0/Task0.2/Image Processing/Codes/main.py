import cv2 as cv
import os
import numpy as np
import csv

def _doTaskA(files):
    data=[]
    for i in files:
        img = cv.imread('../Images/' + i)

        details=img.shape
        intc1 = img[int(details[0]/2)][int(details[1]/2)][0]
        intc2 = img[int(details[0]/2)][int(details[1]/2)][1]
        intc3 = img[int(details[0]/2)][int(details[1]/2)][2]
        data+=[ [i,details[0],details[1],details[2],intc1,intc2,intc3 ]]
    outFile=open('../Generated/stats.csv','w',newline='')
    wt=csv.writer(outFile)
    wt.writerows(data);

def _doTaskB():
    img=cv.imread('../Images/cat.jpg')

    img[:,:,0:2]=[0]
    cv.imwrite('../Generated/cat_red.jpg',img)

def _doTaskC():
    img = cv.imread('../Images/flowers.jpg')
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    img = cv.cvtColor(img, cv.COLOR_RGB2RGBA)
    img[:,:,3]=int(255/2)
    cv.imwrite('../Generated/flowers_alpha.png', img)

def _doTaskD():
    img = cv.imread('../Images/horse.jpg')
    b,g,r=cv.split(img)
    finalp=np.zeros((img.shape[0],img.shape[1]),dtype=b.dtype)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            iVal=((0.3 *img[i][j][2] ) + (0.59 * img[i][j][1])+ (0.11 * img[i][j][0]))
            finalp[i][j]=iVal
    cv.imwrite('../Generated/horse_gray.jpg', finalp)



files=os.listdir('../Images/')
_doTaskA(files)
_doTaskB()
_doTaskC()
_doTaskD()
exit()
