#set operation in multiple set 
#performing union,intersec,symmetric difference


#sets
set1={1,2,3,4,9}
set2={3,4,5,6,9}
set3={5,6,7,9}

#Performing operation 
unionr= set1 | set2 | set3
print(unionr) #all element ignore duplicate 

intersection= set1 & set2 &set3
print(intersection) #common into all

difference= set1 ^ set2 ^ set3
print(difference)