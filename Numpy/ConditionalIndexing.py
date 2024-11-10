import numpy as np

#creating array 
array=np.array([1,2,3,4,5,6,7])

#settig element for condition 

array[array%2==0]=-1 #set even num to -1 

print(array)