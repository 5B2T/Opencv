#阈值算法/二值化算法
import cv2

gray=cv2.imread("bookpage.jpg",cv2.IMREAD_GRAYSCALE)
ret,binary=cv2.threshold(gray,10,255,cv2.THRESH_BINARY)#阈值为10，最大灰度为255

binary_adaptive=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY,115,1)#切割区域 每个区域单独计算阈值 115像素一个区域

ret_otsu,binary_otsu=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#自动计算阈值

cv2.imshow("binary",binary)
cv2.imshow("adaptive",binary_adaptive)
cv2.imshow("otsu",binary_otsu)
cv2.waitKey(0)