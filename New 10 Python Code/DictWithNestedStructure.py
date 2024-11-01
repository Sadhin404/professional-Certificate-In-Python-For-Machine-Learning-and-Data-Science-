#Nested dict 
nested_dict = {
	'person': {
		'name': 'John',
		'details': {
		'age':25, 
		'city':'Dhaka',
		'skills': ['python','Data Analysis']
		}
	}
}


#Accessing nested element
city = nested_dict['person']['details']['city']
#goes to city for access city 
print(city)

#Modifing nested element 
nested_dict['person']['details']['skills'].append('ML Enginner')
print(nested_dict)

