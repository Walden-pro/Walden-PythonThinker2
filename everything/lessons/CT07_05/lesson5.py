#                                                   recap
# food = ["macaroni", "tomato", "chicken", "mcdonalds", "fry"]
# food.pop(2)
# food.append("burgers")
# for i in range(len(food)):
#     print(food[i])

#                                                   task 1 - 3 ->
# import random
# ran = []
# while len(ran) != 100:
#     num = random.randint(1,100)
#     # if num not in ran:
#     ran.append(num)
# print(ran)

# max = max(ran)
# print("maximum score is:", max)
# min = min(ran)
# print("minimun score is:",min)
# ave = sum(ran) / len(ran)
# print("average score is:",ave)

#                                                   task 4 ->
# namelist =   ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan", "Sophia", "Lucas", "Mia", "Aiden"]
# heightlist = [ 160,      165,    158,    170,    162,   168,     159,      172,     164,   166   ]

# maxh = max(heightlist)
# maxhi = heightlist.index(maxh)

# minh = min(heightlist)
# minhi = heightlist.index(minh)

# tn = namelist[maxhi]
# sn = namelist[minhi]

# print(f"tallest person is {tn} their height is {maxh} and their index is {maxhi} ")
# print(f"tallest person is {sn} their height is {minh} and their index is {minhi} ")


#                                                   task 5 ->

pokemons = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax", 
    "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp", "Arcanine", "Alakazam", "Gyarados", "Vaporeon", 
    "Scyther", "Electabuzz"]

powers = [55, 84, 49, 48, 45, 45, 52, 55, 110, 110, 85, 65, 134, 130, 110, 50, 125, 65, 110, 83]

import random
rp = random.choice(pokemons)
rp2 = rp
while rp == rp2:
    rp2 = random.choice(pokemons)

print(rp, rp2)
rpn = rp
rp2n = rp2


rp = pokemons.index(rp)
rp2 = pokemons.index(rp2)



rpp = powers[rp]
rp2p = powers[rp2]

print(f"{rpp}        {rp2p}")


if rpp > rp2p:
    print(rpn,"wins")
else:
    print(rp2n,"wins")

