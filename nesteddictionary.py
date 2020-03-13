# Name: Fawaz
# Class: CS30
# Topic: RPG Nested Dictionary
# Date: March 10, 2020

# This code prints the characters name, age and city
character = {'Name' :'John',
             'Age': '24',
             'City': 'Regina'}

for word in character:
    print(word + ": " + character[word])
#This character prints the protections and Decisions
description ={'Protection':'John has 100 health points',
              'Decision' : 'For every wrong decision, John looses 5 points'}

for word in description:
    print(word + ": " + description[word])

#This code prints the Locations John went to
locations = {'Location':'''Johns is schooling at the University of Regina which
             closes at 2:30pm. He will go straight to his house after school
             which is in Habour Landing. After he gets home, he will start
             having a stomach pain which he will be rushed to the
             hospital using the Emergency medical service'''
             }
print(locations)
Inventory = {'Health' : '100',
             'Damages':'5',
             'Damages after coming back from the Hospital': '3' ,
             'Pizza': '7',
             'Description': 'For every pizza eaten, there will be 7 damages'}
for word in Inventory:
    print(word + ": " + Inventory[word])
     
