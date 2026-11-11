#模型匹配
import cv2
import numpy as np

image=cv2.imread("poker.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

template=gray[65:100,360:387]

match=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)#标准相关匹配算法
locations=np.where(match>=0.9)#匹配度大于等于0.9

h,w=template.shape[0:2]#长 宽
for p in zip(*locations[::-1]):
    x1,y1=p[0],p[1]
    x2,y2=x1+h,y1+w
    cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("image",image)
cv2.waitKey()