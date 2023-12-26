def min_max_sum_len(*args, list_of_nums):
    min_num = args[0]
    len_num = 0
    max_num = args[0]
    sum_nums = 0
    
    for i in args:
        sum_nums += i

        len_num += 1

        if i > max_num:
            max_num = i
        
        if i < min_num:
            min_num = i

        list_of_nums.append(i)

    print(min_num, max_num, sum_nums, len_num)

list_nums = [11]

min_max_sum_len(1,12,15,18,list_of_nums = list_nums)
print(list_nums)



    
