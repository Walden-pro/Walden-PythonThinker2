#                           recap ->
# student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]
# new_index=[]
# sr=0

# for student in student_indexes:
#     if student not in new_index:
#         new_index.append(student)
#         sr=sr+1

# sr = len(student_indexes) - sr
# print(new_index)
# print(f"dupes removed: {sr}")
# print(f"{len(new_index)} students attended class")

#                   task 1a,1b,1c ->

# while True:
#     name=input("your first name: ")
#     if name.isalpha():
#         print("this is a valid name")
#         break
# while True:
#     age=input("your age: ")
#     if age.isdigit():
#         print("this is a valid age")
#         break
# while True:
#     un=input("your username: ")
#     if un.isalnum():
#         print("this is a valid username")
#         break

#                   task 2a,2b ->
# while True:
#     pn=input("your phone number: ")
#     if pn.isdigit() and len(pn) == 8:
#         print("this is a valid phone number")
#         break

# while True:
#     un=input("your username: ")
#     if un.isalnum() and len(un) > 4 and len(un)<19:
#         print("this is a valid username")
#         break
#                   task 3a,3b ->

# while True:
#     by=input("your birth year: ")
#     if by.isdigit() and int(by) > 1899 and int(by) < 2027:
#         print("this is a valid birth year")
#         break

# while True:
#     by=input("your volume: ")
#     if by.isdigit() and int(by) > -1 and int(by) < 101:
#         print("this is a valid volume")
#         break

#                   task 4 ->
sen = input("a sentence: ")
for char in sen:
    for i in range(len(sen)):
        if i % 2 == 0:
            char = char.upper()
    
    
print(char)

#                   task 5 ->



#                   task 6 ->



#                   task 7 ->



#                   task 8 ->



#                   task 9 ->


