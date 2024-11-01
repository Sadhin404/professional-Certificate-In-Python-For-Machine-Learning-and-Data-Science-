#we can store multiple value into single variable
# using *before variable name 

tuple=('Shadhin',21,'Jhenaidah','CSE','Single')

#unpacking 
name,age,*other=tuple

print('Name:',name)
print('Age:',age)
print('Other:',other)

#Value from tuple will be stored in the variable 
#other details will be saved into Other variable 