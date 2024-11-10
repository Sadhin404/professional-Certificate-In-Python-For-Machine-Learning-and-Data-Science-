import numpy as np 

array=np.array([0,1,2,3])
choices= [array*2,array+20,array**2]

result=np.choose(array,choices)
print("choose:",result)