import cv2

image=cv2.imread("demo_output.png")

crop=image[10:170,40:200]#前一个选第几列到第几列 后一个选行
cv2.imshow("crop",crop)

cv2.waitKey()