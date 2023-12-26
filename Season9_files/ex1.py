count = 0
scores = 0
print("--- current grades ---")
with open("grades.txt") as reader:
    all_data = reader.read()
    print(all_data)
    
user_add = input("add another grades: ")
print("-" * 15)

if user_add.lower() == "y": 
    with open("grades.txt", "a") as grades_file:
        while True:
            user_input = input("enter name: ")

            if str(user_input) == "exit":
                break

            user_score = input(f"[{user_input}] score is : ")
            scores += int(user_score)
            count += 1
            print("-" * 15)
            grades_file.write(f"\n{user_input} {user_score}")

else:
    print("bye")


my_list = []
with open("grades.txt") as gf:
    for line in gf:
        line = line.rstrip("\n").split(" ")
        my_list.append(int(line[1]))

    print(f"The avrage is {sum(my_list) / len(my_list)}")