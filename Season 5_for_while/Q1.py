while True:

    is_prime = False
    
    user_num = int(input("enter your number: "))
    for i in range(2,int(user_num / 2)):
        if user_num % i == 0:
            is_prime = True
            break

    if is_prime == True:
        print("Not prime")
    else:
        print("Is prime")