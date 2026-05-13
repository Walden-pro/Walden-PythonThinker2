#                                       recap ->
# import random
# ran = []
# while len(ran) != 100:
#     num = random.randint(1,1000)

#     if num not in ran:
#         ran.append(num)
    

# print(ran)

# max = max(ran)
# print(f"maximum score is: {max}")
# maxi = ran.index(max)
# print(f"max number index is: {maxi}")
# min = min(ran)
# print(f"mininun score is: {min}")
# mini = ran.index(min)
# print(f"min number index is : {mini}")
# ave = sum(ran) / len(ran)
# print(f"average score is: {ave}")

# rc = random.choice(ran)
# print(f"the random choice is: {rc}")
# rci = (ran.index(rc))
# print(f"the random choice index is: {rci}")


#                                       task 1 ->

# contacts = []
# contact1 = ["John",   98453126, "john@gmail.com"]
# contact2 = ["Adam",   93029102, "adam@gmail.com"]
# contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]
# contacts.append(contact1)
# contacts.append(contact2)
# contacts.append(contact3)

# for contact in contacts:
#     name, number, email = contact
#     print(name,number,email)

#                                       task 2 ->
# students = [
#     ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
#     ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],["Sophia", "F"], 
#     ["Lucas", "M"], ["Mia", "F"],["Aiden", "M"], ["Isabella", "F"], 
#     ["Jackson", "M"],["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
# ]

# for student in students:
#     name, gender = student
#     print(f"Gender of {name} is {gender}")
#                                       task 3 ->
students = [
    ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
    ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],["Sophia", "F"], 
    ["Lucas", "M"], ["Mia", "F"],["Aiden", "M"], ["Isabella", "F"], 
    ["Jackson", "M"],["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
]

boys = []
girls = []
for student in students:
    name, gender = student
    if gender == "M":
        boys.append(student)
    else:
        girls.append(student)

for boy in boys:
    name, gender = boy
    print(name)

for girl in girls:
    name, gender = girl
    print(name)

print(f"there are {len(boys)} boys")
print(f"there are {len(girls)} girls")
