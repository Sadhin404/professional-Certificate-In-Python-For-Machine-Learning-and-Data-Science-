import numpy as np 

#creating mashgrid
x=np.array([1,2,3])
y=np.array([4,5,6])

#creating mash
x,y=np.meshgrid(x,y)


print(x)
print("-----------")
print(y)