#3d
import numpy as np
arrayy=np.array([[[1,4],[3,4]],
                 [[5,6],[7,8]]])

#access
ele=arrayy[1,1,1] #element at 1,0,1

#slice
slice=arrayy[:,0,:]

print(ele)
print("------------------")
print(slice) 