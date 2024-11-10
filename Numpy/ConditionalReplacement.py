import numpy as np

#creating array 
array=np.array([1,2,3,4,5,6,7])

#replacing element based on  condition 

result = np.where(array>5,99,array)

print(result)