def divisor(num):
    my_list = list()
    for i in range(1, num + 1):
        if num % i == 0:
            my_list.append(i)

    return my_list

print(divisor(6))