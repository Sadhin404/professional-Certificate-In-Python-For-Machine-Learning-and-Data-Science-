import numpy as np

#3x3
array= np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]])

#slice using row and col

select=array[1:,:2]
print(select) 