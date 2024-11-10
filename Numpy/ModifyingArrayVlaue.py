import numpy as np 
array= np.array([1,-2,3,-4,5])

#modifying value by index 

array[[1,3]]=[1000,3000]

print(array)
array[4]=99
print(array)