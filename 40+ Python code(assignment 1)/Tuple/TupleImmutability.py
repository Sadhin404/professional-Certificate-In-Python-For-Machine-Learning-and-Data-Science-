tuple = (6,9,1)

#tuple value cannot be change after created it will give error 

try:
tuple[0]= 10
except TypeError as e:
	print ('Error', e)