from random import randint

user_cup = int(input("enter many cups? "))
user_chance = int(input("how many chances? "))

print("-"* 12)

ai_cup = randint(1,user_cup)
winner = False

while user_chance > 0:

    if user_chance > 1:
        print(f"{user_chance} chances left.")
    else:
        print(f"{user_chance} chance left.")

    user_choice = int(input(f"Guess [1 - {user_cup}]: "))
    if user_choice == ai_cup:
        print("You guessed right.")
        winner = True
        print("-"* 12)
        break
    else:
        print("Wrong guess.")
        user_chance -= 1

    print("-"* 12)


if winner == True:
    print("You won!")
else:
    print(f"The right answer is {ai_cup}")
    print("You lost. Sorry!")