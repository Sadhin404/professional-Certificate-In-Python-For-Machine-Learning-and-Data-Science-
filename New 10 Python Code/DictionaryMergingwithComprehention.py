#dictionary
dict1= {'a': 1, 'b': 2,'c':3}
dict2= {'b': 4,'c': 5,'d': 6}

#Merging and modifying 
merge= {key: dict1.get(key,0)+ dict2.get(key,0)
		for key in set (dict1) | set(dict2)}


print(merge)