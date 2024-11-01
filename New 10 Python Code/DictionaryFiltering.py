#example dictionary
scores={'Ron' : 86, 'Lio' : 69, 'Newton' : 33}

#filtering with condition >=80
filterr= {name : score for name, score in scores.items() if score >=80}


print(filterr)