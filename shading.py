import numpy as np
import cv2
image=cv2.imread(r'C:\Users\Jyothi\Desktop\Tulips.jpg')
x=cv2.imread(r'C:\Users\Jyothi\Desktop\Grey002.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
x=cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)
x=np.float16(x)-x.min()
x=x/255

image=np.uint8(image*x)
cv2.imshow('heal',image)
cv2.waitKey(0)
