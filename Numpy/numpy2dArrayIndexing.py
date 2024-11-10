#2d array indexing 
import numpy as np
arrayy= np.array([[4,7,8], 
                  [2,3,4], 
                  [8,6,5]]) #2d
#accessing element 
ele=arrayy[1,1]

#slicing row colloumn 
rowslice=arrayy[0,:] #ROW
coloumnslice=arrayy[:,1] #COLLOUMN

print(ele)
print(rowslice)
print(coloumnslice)