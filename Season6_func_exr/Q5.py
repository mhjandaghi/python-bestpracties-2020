def lozi_saz(num):
    for char in range(num):
        print(" " * (num - char), "*" * (2 * char + 1))
    for i in range(num - 2, -1, -1):
        print(" " * (num - i), "*" * (2 * i + 1))

# lozi_saz(4)

def print_star_line(num_star, total_start):
    num_space = int((total_start - num_star) / 2)
    print(" " * num_space, end="")
    print("*" * num_star)


def lozi_fard(num):
    print()
    num_of_stars = None
    if num % 2 == 0:
        num += 1
    for i in range(num):
        if i < num / 2:
            num_of_stars = i * 2 + 1
        else:
            num_of_stars = ((num - i) * 2 - 1)
        print_star_line(num_of_stars, num)

    print() 


lozi_fard(6)

