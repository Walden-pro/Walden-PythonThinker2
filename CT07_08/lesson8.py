#                           recap ->
# student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]
# new_index=[]
# sr=0
# not_unique = []
# for student in student_indexes:
#     if student not in new_index:
#         new_index.append(student)
#         sr=sr+1
#     else:
#         not_unique.append(student)

# sorted = sorted(new_index)
# print(sorted)

# # group all the student indexes such that it is in ascending order 
# # if there is more than once, put them together, for example if there is two 1042, they should be in [1042,1042]
# # the final result is a nested list where by those with duplicate are in [1042,1042] manner 
# # and those unique would be in [1043] manner and the nested list will be [[1042,1042], [1043], ...]

# nested_list = []

# for index in new_index:
#     if index in not_unique:
#         for i in range(2):
#             nested_list.append(index)
#     else:
#         nested_list.append(index)

# print(nested_list)
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
#     if not un.isalpha() and not un.isdigit() and un.isalnum() and len(un) > 5 and len(un)<20:
#         print("this is a valid username")
#         break
#     elif len(un) < 5:
#         print("length of username is too short")
#     elif len (un) > 20:
#         print("length of username is too long")
#     elif un.isalnum():
#         print("username should contain both alpha and num")
#     else:
#         print("username should not contain special character")


# find out how to allow user to have both alphabet and number
# no allow: 33434423, sadoadha 
# isalpha -> false
# isdigit -> false
# isalnum -> true
# length requirement -> 6 - 19
# asdadasds: print it should contain both alpha and num
# 1121321: same as above
# the length does not meet requirement: print length does not meet requirement, too long or too short
# if got special character: print it should not contain special character or print it should contain both alpha and num

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
# sen2 = ""
# sen = input("a sentence: ")

# for i in range(len(sen)):
#     if i % 2 == 0:
#         char = sen[i].upper()
#         sen2 = sen2 + char
#     else:
#         char = sen[i].lower()
#         sen2 = sen2 + char

# print(sen2)



#                   task 5 ->
# word = "SINGAPORE"
# print(word[:4])
# print(word[3:6])
# print(word[5:])
# print(word[::2])
#                   task 6 ->


# while True:
#     user_input = input("input a word: ")
#     if user_input == user_input[::-1]:
#         print("it is a palindrome")
#     elif user_input == "end":
#         break
#     else:
#         print("it is not a palindrome")

#                   task 7 ->
# fl = ["geng woon", "p","diddy","yihao","elliot"]
# fp = 0
# while True:
#     inputs = input("your name:")
#     if inputs == "":
#         print("pls enter a name ")
#     if inputs in fl:
#         fp=fp+1
#         print("you are accepted")
#     else:
#         print("your entry was denied get out")
#     if fp == 5:
#         print("everybody was here")
#         break

#                   task 8 ->
flu = False
fcv = False
sdib = False
nll = False

nric = input("What is the nric that u have")
if len(nric)!= 9:
    nll = True
    if nric[1:8].isalpha():
        print("the seven characters must be digits.")
    if nric[0]!="S" or nric[0]!="T" or nric[0]!="F" or nric[0]!="G" or nric[0]!="M":
        print("first alphabet of nric must be stfgm")
    if nric[0].islower():
        print("first alphabet of nric must be upper case")
    if nric[8].isdigit():
        print("last letter of nric must be alphabet.")
    if nric[8].islower():
        print("last letter of nric must be the upper case")
    else:
        print("this is a valid nric")
    



#                   task 9 ->

# while True:
#     un=input("your password: ")
#     if not un.isalpha() and not un.isdigit() and un.isalnum() and len(un) > 7 and
        
#     elif len(un) < 7:
#         print("length of password is too short")

#     elif un.isalnum():
#         print("password should contain both alpha and num")
#     else:
#         print("password should not contain special character")
