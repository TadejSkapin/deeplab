import cv2
import numpy as np
from PIL import Image

#'''
#img = cv2.imread('00000811.png',-1)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
#b,g,r = cv2.split(img)
img = cv2.imread('000097_prediction.png',-1)
#cv2.imshow('image', img)
cv2.waitKey(1)
print('Blue')
print(img[128:200,128:200,0])
print('Green')
print(img[128:200,128:200,1])
print('Red')
print(img[128:200,128:200,2])
#'''
'''
img = cv2.imread('2007_001321.png',-1)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
#b,g,r = cv2.split(img)
cv2.imshow('image', img)
cv2.waitKey(1)
print('Blue')
print(img[128:200,128:200,0])
print('Green')
print(img[128:200,128:200,1])
print('Red')
print(img[128:200,128:200,2])
'''
'''
img = cv2.imread('2007_001321r.png',-1)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
#b,g,r = cv2.split(img)
cv2.imshow('image', img)
cv2.waitKey(1)
print('Blue')
print(img[128:200,128:200])
##print('Green')
##print(img[128:200,128:200,1])
##print('Red')
##print(img[128:200,128:200,2])


#img = Image.open('2007_000032.png')
#print(img)
'''
