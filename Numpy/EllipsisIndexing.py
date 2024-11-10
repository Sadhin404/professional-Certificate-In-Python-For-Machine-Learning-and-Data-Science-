import numpy as np 

#3d array
array = np.array([[[1,2],[3,4]],
                  [[5,6],[7,8]],
                  [[9,10],[11,12]]])

result=array[..., 1]
print(result)