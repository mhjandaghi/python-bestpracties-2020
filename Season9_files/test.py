my_file = open("pedar.txt", "r+")
my_list = my_file.read().split("\n")

# while True:
#     a = my_file.readline()
#     if a == "":
#         break
#     my_list.append(a.rstrip("\n"))
# while True:
#     user_input = input("enter name: ")
#     if user_input == "exit":
#         break
#     my_list.append(user_input)

# print(my_list)
#=============================
# import sys
# sys.stdin = open("pedar12.txt", "r")
# m = sys.stdin.readline()
# print(m)
# z = input()
# print(z)
# --------------------
import json
name = "ali"
age = 12
marks = {"riazi": [12, 14 ,16], "pyhsics": [10,17,16.5]}
lessons = ["math", "sport", "history"]
b = False
final_dict = {
    "name": name,
    "age": age,
    "b": b,
    "lessons": lessons
}
with open("json1.json", "w") as jsf:
     json.dump(final_dict, jsf, indent= 4)

with open("json1.json") as jf:
    s = json.load(jf)

name1 = s["name"]
age1 = s["age"]
