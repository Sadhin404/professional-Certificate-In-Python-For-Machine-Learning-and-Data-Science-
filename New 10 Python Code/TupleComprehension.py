#Create tuple using range 
my_tuple=range (1,11)
print(my_tuple) #test for before 

#tuple of square but even number only
evensqure= tuple(i**2 for i in my_tuple if i%2==0)

print(evensqure)