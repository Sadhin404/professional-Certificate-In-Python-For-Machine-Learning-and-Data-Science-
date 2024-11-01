matrix = [[1,2,3], [4,5,6], [7,8,9]]
#matrix 

#Flattering even num,ber with loop 
even=[num for row in matrix for num in row if num%2==0]

print(even)
