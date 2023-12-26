my_file = open("cont.txt", "r+")
my_list = sorted(my_file.readlines())
new_file = open("new_cont.txt", "w+")

def edit_text_cities(list_of_cities):
    for line in list_of_cities:
        line.rstrip("\n").lower()
        new_file.write(line)

edit_text_cities(my_list)
test_list = open("new_cont.txt", "r+")
list_of_edit_contry = test_list.readlines()

def binary_search_from_list(my_list, low, high, x):
    if high > 1:
        mid = int(low + (high - 1) / 2)

        if my_list[mid][0] == x:
            return my_list[mid][1]
        
        elif my_list[mid][0] > x :
            return binary_search_from_list(my_list, low, mid - 1, x)
        
        else:
            return binary_search_from_list(my_list, mid + 1, high, x)
        
    else:
        return -1
    

# print(binary_search_from_list(sorted_list, 0, len(sorted_list) - 1 , "a"))



