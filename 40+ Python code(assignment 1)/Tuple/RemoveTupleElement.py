my_tuple = (1,2,3,5,7,8,9)

#immutable to remove convert tuple into list 

my_list = list(my_tuple)
my_list.remove(7)

my_tuple= tuple(my_list)
print (my_tuple)