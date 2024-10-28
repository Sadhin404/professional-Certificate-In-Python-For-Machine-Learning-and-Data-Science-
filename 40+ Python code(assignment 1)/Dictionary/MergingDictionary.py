dict= {'name' : 'shadhin' , 'age' : 22, }
dict2 = {'city' : 'jhenaidah'}

dict.update(dict2)  # we can merge by update() or **

print('Merge done ', dict)  #only work for python version 3.9+