#  SWAPPING A CROPPED PART OF IMAGE

import cv2
p1=cv2.imread('p1.jpg')
cv2.imshow('PICTURE-1',p1)
cv2.waitKey()
cv2.destroyAllWindows()
p2=cv2.imread('p2.jpg')
cv2.imshow('PICTURE-2',p2)
cv2.waitKey()
cv2.destroyAllWindows()

p1=cv2.imread('p1.jpg')
pic1=p1[50:400,500:750]
cv2.imshow('PICTURE-1',pic1)
cv2.waitKey()
cv2.destroyAllWindows()

p2=cv2.imread('p2.jpg')
pic2=p2[150:500,400:650]
cv2.imshow('PICTURE-2',pic2)
cv2.waitKey()
cv2.destroyAllWindows()

p1=cv2.imread('p1.jpg')
p1[50:400,500:750]=pic2
cv2.imshow('PICTURE-1',p1)
cv2.waitKey()
cv2.destroyAllWindows()

p2=cv2.imread('p2.jpg')
p2[150:500,400:650]=pic1
cv2.imshow('PICTURE-2',p2)
cv2.waitKey()
cv2.destroyAllWindows()