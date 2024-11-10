import numpy as np 
array= np.array([1,-2,3,-4,5])

#creating mask of pos value 
mask=array>0

print(array[mask])