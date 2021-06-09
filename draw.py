#  DRAWING A STAR

import cv2
import numpy as n

pic=n.zeros((1080,1920,3), dtype='uint8')
cv2.line(pic,(200,400),(500,400),(0,255,0),10)
cv2.line(pic,(200,400),(350,100),(0,255,0),10)
cv2.line(pic,(500,400),(350,100),(0,255,0),10)
cv2.line(pic,(200,200),(500,200),(0,255,0),10)
cv2.line(pic,(500,200),(350,500),(0,255,0),10)
cv2.line(pic,(350,500),(200,200),(0,255,0),10)

cv2.imshow('DRAWING',pic)
cv2.waitKey()
cv2.destroyAllWindows()