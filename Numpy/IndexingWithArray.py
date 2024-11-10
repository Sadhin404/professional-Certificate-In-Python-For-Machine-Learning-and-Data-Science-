import numpy as np 

#creating 2d array
array=np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])

#using array for indexing 
rows=np.array([0,1,2])
cols=np.array([2,1,0])
indexes=array[rows,cols]

print(indexes)