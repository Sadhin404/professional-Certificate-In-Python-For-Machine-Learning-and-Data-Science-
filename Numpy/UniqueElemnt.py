import numpy as np 
array= np.array([1,2,2,3,4,4,4,5])

#unique element 
unique,counts=np.unique(array,return_counts=True)

print(unique)
print(counts)