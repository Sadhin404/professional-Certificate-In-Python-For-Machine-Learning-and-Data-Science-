import numpy as np

#1d
ar=np.array([1,2,3,5])
ar2=np.array([7,8])

#mashgrid
x,y = np.meshgrid(ar,ar2)
indices=np.vstack([x.ravel(), y.ravel()])

print(indices)