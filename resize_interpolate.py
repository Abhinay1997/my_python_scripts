import numpy as np
import cv2

image=cv2.imread(r'C:/Users/Jyothi/Downloads/pexels-photo.jpeg')
res=cv2.resize(image,(1200,768),interpolation=cv2.INTER_CUBIC)
cv2.imshow('late',res)
cv2.waitKey(0)
