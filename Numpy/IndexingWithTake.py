import numpy as np

array=np.array([10,20,30,40,50])

#Using np.take to select element ad spacific indices

indices=[0,2,4]
result= np.take(array,indices)

print(result)