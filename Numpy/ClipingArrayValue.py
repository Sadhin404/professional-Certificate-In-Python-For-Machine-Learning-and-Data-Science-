import numpy as np 

array=np.array([1,3,4,5,7])


#clipping value betweer  2 ,4
clipar=np.clip(array,2,4)

print(array)
print("new:",clipar)