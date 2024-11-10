import numpy as np

array=np.array([10,20,30,40,50])

#Using np.where to find spacific value based on condition 

indices=np.where(array>25)
print(array[indices])