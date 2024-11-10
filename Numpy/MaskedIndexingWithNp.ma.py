import numpy as np 
array= np.array([1,-2,3,-4,5])

#maskng element where valur are negative 
maskedar=np.ma.masked_where(array<0,array)

print(maskedar)