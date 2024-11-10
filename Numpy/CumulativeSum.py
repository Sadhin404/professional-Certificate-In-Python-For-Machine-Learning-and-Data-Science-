import numpy as np

#creating array 
array=np.array([1,2,3,4,5,6,7])

#cumulative sum
cumulativesum=np.cumsum(array)
cumulativeprod=np.cumprod(array)



print(cumulativesum)
print(cumulativeprod)