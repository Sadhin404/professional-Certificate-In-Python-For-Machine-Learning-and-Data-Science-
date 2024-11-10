import numpy as np 

array=np.array([10,15,20,25,30,35])

#bool condition
result= array[(array>10) & (array <30)][[0,2]]

print(result)