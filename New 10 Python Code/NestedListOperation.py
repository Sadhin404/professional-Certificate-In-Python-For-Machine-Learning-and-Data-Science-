#example nested list 
nested_list=[[1,2,3],[4,5,[6,7]],[8,9]]
print(nested_list) #checking 

#accessing 
nested_ele= nested_list[1][2][1]
#[1] is the which list by index so its 2nd list 
#[2] is the [4,5,[6,7] 6 by index 
#[1] is 2nd index value which is 7
print(nested_ele)
print(nested_list[2][1]) #9


#Modifying 
nested_list[2][1]=10 #change 9 to 10
print('Changer value:',nested_list[2][1])


#Flattening list 
flattened_list = [element 
for sublist in nested_list
for item in sublist
for element in (item if isinstance(item, list) else [item])]
#confusing
print(flattened_list)