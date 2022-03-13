# Logical Operators in Python are weird, they use the words ' and', 'or' and' not' intead of &&, || and !
print(5<3 and 5==5)
print(5<3 or 5==5)
print(not 5 < 3)

#print(2==2 && 3==3) #generates invalid syntax error

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density > rio_de_janeiro_pop_density)
print(not san_francisco_pop_density > rio_de_janeiro_pop_density)