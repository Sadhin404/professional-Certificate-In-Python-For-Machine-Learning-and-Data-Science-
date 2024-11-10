import numpy as np 

array =np.array([10,20,3,40,5,60,70])

#Bool indexing 
even_num=array[array % 2==0]

print(even_num)