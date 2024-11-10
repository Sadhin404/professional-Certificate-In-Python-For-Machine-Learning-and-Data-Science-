import numpy as np

arrayy=np.array([[1,2,3,4],[5,6,7,8],
               [9,10,11,12]])
               
#slicing
result=arrayy[::2,::2] #::2 skip
print(result)