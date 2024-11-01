#List of tuple 

tuple_list=[('a',1),('b',2),('c',3),('d',4)]

#converting to dictionary 
my_dictionary= {key:value for key , value in tuple_list}
#it will itterate over the list tuple for key and value 
#and stotre it in my_dictionary

print(my_dictionary)