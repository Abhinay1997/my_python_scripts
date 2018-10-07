import pyautogui
import matplotlib.pyplot as plt
from time import sleep
temp_x=[]
temp_y=[]
pyautogui.moveTo(1366/2,768/4,0.05)
for i in range(90):
    x = pyautogui.position()
    sleep(0.025)
    y=(a,b)=pyautogui.position()
    if x!=y:
        temp_x.append(a)
        temp_y.append(b)
        print(a,b)
plt.plot(temp_x,temp_y,'ro')
plt.axis([0,1366,768,0])
plt.show()
        
        
    
