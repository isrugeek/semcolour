import cv2
import sys
import os
import numpy as np




source = '../cnn_transfer/sem/'
output = '../cnn_transfer/sem_gray/'
file = 0
for filename in os.listdir(source):
    image = cv2.imread(source+filename)
    rgb = cv2.cvtColor(image,cv.COLOR_RGB2BGR)
    lab = cv2.cvtColor(rgb,cv2.COLOR_BGR2LAB)
    # gray = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
    # gray = cv2.cvtColor(gray,cv2.COLOR_RGB2LAB)
    # gray = cv2.cvtColor(gray,cv2.COLOR_LAB2RGB)
    # gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    #         cv2.THRESH_BINARY,255,2)


    #print (gray.shape)
    #print(size.gray)
    #lab_image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    l_channel, a_channel, b_channel = cv2.split(gray)

    # cv2.imshow("RGB",image)
    cv2.imshow("LAB",lab)

    cv2.imshow("L",l_channel)
    cv2.imshow("A",a_channel)
    cv2.imshow("B",b_channel)
    cv2.waitKey(0)

    cv2.imwrite(output+str(file)+".jpg",lab)
    file+=1

'''
image = cv2.imread('../dataset/resized/0.jpeg')
# I was uncertain if it was BGR or RGB but in this case it doesn't matter because
# of my input image.
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
l_channel,a_channel,b_channel = cv2.split(lab_image)


cv2.imshow("LAB",lab_image)
cv2.waitKey(0)


'''
