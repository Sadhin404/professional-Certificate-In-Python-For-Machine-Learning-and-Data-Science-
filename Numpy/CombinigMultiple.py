import numpy as np 
arrayy=np.array([[10,20,30],[40,50,60],[70,80,90]])

#combining boolean fancy
result= arrayy[arrayy>30][:,[0,2]]

print("result",result)