## Task 1: List of planets
# **Task: Create a list of 8 planets in the solar system**

# **Task 1a**:
# Create a list of 8 planets in the solar system.
# (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune)
# planets = ["mercury", 
#            "venus",
#            "earth",
#            "mars",
#            "jupiter", 
#            "saturn", 
#            "uranus", 
#            "neptune"]
# print(planets)
# **Task 1b**:
# You have conquered Mars, **rename** Mars to a name of
# your liking
# planets[3] = "ur mars"
# print(planets)
# **Task 1c**:
# 1. You have decided Pluto is a planet again, **add** Pluto
#    into the list
# planets.append("pluto")
# print(planets)
# 2. You created an artificial planet between Earth and
#    Mars called "Lalaland". **Insert** the planet in
#    correctly into the list.
# planets.insert(3, "lalaland")
# print(planets)
# **Task 1d**:
# You launched a war againts Jupiter and destroyed it,
# **delete** Jupiter from the list
## Task 2: List of planets (part 2)
# planets.pop(5)
# print(planets)






## Task 2: List of planets (part 2)
# Tasks:

# 1. Write a for loop and print out all the names of the
#    planets
# 2. If name == "Earth", print "<planet name> : this is
#    my home"
# 3. If name == "Mars" (or changed name), print
#    "<planet name> : I conquered this"
# 4. If name == "Lalaland", print
#    "<planet name> : I created this"

# for i in range(len(planets)):
#     if planets[i] == "earth":
#         print(planets[i] +": this is my home")
#     elif planets[i] == "ur mars":
#         print(planets[i] +": i conquered this")
#     elif planets[i] == "lalaland":
#         print( planets[i] +": i created this")
#     else:
#         print(planets[i])


## Task 3: Flight Round the Globe
# Task: Write a program to keep track of the countries you
# are visiting.

# 1. Use a while loop to ask the user what country they
#    would like to visit.
# 2. Add the country into a list
# 3. If the user types "end", exit the loop
# 4. Print all the countries in the list in this format.
#    "I would like to visit Germany"
#    "I would like to visit Japan"
#    ... 

# countries = []
# while True:
#     u = input("what country u will like to visit")
#     if u == "end":
#         for i in range(len(countries)):
#             print("i would like to visit "+countries[i])
            
#     countries.append(u)
    


## Task 4: Restaurant Menu
# **Task 4a**:
# Write a program to create a menu for a new
# restaurant

# 1. Using a while loop, ask the user (the restaurant manager)
#    to input food items
# 2. Add each food item into the menu list
# 3. End the loop when the user types "end"

#_________________________________
# **Task 4b**:
# Based on the list created by the restaurant manager, do
# the following:

# 1. Imagine a customer has come in, ask the customer what
#    would they like to eat?
# 2. If the food is in the list, say "Yes we sell that,
#    please have a seat"
# 3. else, say "Sorry, please go next door, bye."


f = []
while True:
    u = input("what is in menus: ")
    if u == "end":
        for i in range(len(f)):
            print("the menu has: "+f[i])
        break    
    f.append(u)

c = input("what will you like: ")
while True:
    if c in f:
        print("we have that, pls take a seat now.")
        break
    else:
        print("sorry we dont have that. pls go the next door now")
        break

