#形态学算法 腐蚀和膨胀
import cv2
import numpy as np

gray=cv2.imread("opencv_logo.jpg",cv2.IMREAD_GRAYSCALE)

_,binary=cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)#反向阈值
kernel=np.ones((5,5),np.uint8)#5*5操作核

erosion=cv2.erode(binary,kernel)#腐蚀
dilate=cv2.dilate(binary,kernel)#膨胀

cv2.imshow("binary",binary)
cv2.imshow("erosion",erosion)
cv2.imshow("dilate",dilate)

cv2.waitKey(0)