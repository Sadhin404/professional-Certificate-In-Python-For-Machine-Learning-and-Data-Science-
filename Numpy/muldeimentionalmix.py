import numpy as np

#3x3
array= np.array([[[1,2],[3,4]],
                 [[5,6],[7,8]],
                 [[9,10],[11,12]]])

#slicing with direct indexing 
mixed=array[1:,0,1]
print(mixed) 