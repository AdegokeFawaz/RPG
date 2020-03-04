# Name: Fawaz
# Class: CS30
# Teacher's Name: Ms. Cotcher
# Date Modified: February 22, 2020


#This code prints the names of the employers
employers = ['John', 'Sam', 'Peter']
print(employers[0])
print(employers[1])
print(employers[2])

#This code adds Raza to the employer lists
employers.append('Raza')
print(employers)

#This code adds Fawaz name to the code and makes him the second employer
employers.insert(1, 'Fawaz')
print(employers)

#This code will remove peters name from the list
del employers[3]
print(employers)

#This program removes and return the second name
return_name = employers.pop(2)
print(employers)

#This code removes Fawaz name from the code
employers.remove('Fawaz')
print(employers)
#This code sorts the employer names and will also switch the last name with the first name
employers.sort()
print(employers)
print(sorted(employers))
employers.reverse()
print(employers)
print(len(employers))
