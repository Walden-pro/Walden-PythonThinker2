#                           recap ->

# students = []
# student1 = ["James", 85726845 ,"Hockey"]
# student2 = ["Danny", 67676767 ,"Basketballs"]
# student3 = ["Ben",   69696969 ,"Footballs"]
# students.append(student1)
# students.append(student2)
# students.append(student3)
# for student in students:
#     name, number, cca = student
#     print(f"Name:{name}")
#     print(f"Phone number:{number}")
#     print(f"CCA:{cca}")

#                           task 1 ->

# list1 = ["Apple", "Banana", "Cherry"]
# list2 = ["Durian", "Elderberry", "Figs"]


# inv = list1+list2
# print(inv)

#                           task2->

# list1 = [3.20, 2.65, 1.75]
# list2 = [6.15, 5.45, 4.20]

# inv=list1+list2
# sorteds = sorted(inv)
# print(sorteds)

#                           task3->

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# index = 3
# print(fruits[:index])
# print(fruits[index:])

#                           task4->
# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# mid = len(fruits) // 2
# print(fruits[:mid])
# print(fruits[mid:])
#                           task5->
# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]
# common = []
# for fruit in list1:
#     if fruit in list2:
#         common.append(fruit)
# print(common)
#                           task6->

# list1 = ["Apple", "Banana", "Cherry", "Cherry"]
# list2 = ["Cherry", "Durian", "Durian", "Figs"]
# unique = []
# for fruit in list1:
#     if fruit not in unique:
#         unique.append(fruit)
# for fruit in list2:
#     if fruit not in unique:
#         unique.append(fruit)
# print(unique)
#                           task7->
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# lists = list1+list2
# even=[]
# for number in lists:
#     if number % 2 == 0:
#         even.append(number)
# print(even)
#                           task8->
# flattened_list = []
# nested_list = [[1, 2], [3, 4], [5, 6]]
# for lists in nested_list:
#     for number in lists:
#         flattened_list.append(number)
# print(flattened_list)
#                           task9->

students = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ns=[]
size = 3

for i in range(0,len(students),size):
    ns.append(students[i:i+size])
print(ns)