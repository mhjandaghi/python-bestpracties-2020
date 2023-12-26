from random import choice

l_game = ['sang', 'kaqaz', 'qeychi']
dict_game = {'s': l_game[0],
            "k": l_game[1],
            'q': l_game[2] }

user_point = 0
ai_point = 0

while user_point < 3 and ai_point < 3:
    print()
    user_choice = input("enter your choice('s' 'k' 'q'): ")
    ai_choice = choice(l_game)

    if user_choice in dict_game.keys():
        print(f"Ai choice is {ai_choice} and your choice is {dict_game[user_choice]}")

        if (user_choice == 's' and ai_choice == l_game[2]) or (user_choice == 'k' and ai_choice == l_game[0]) or (user_choice == 'q' and ai_choice == l_game[1]) :
            user_point += 1
            print("user +1")
        elif (ai_choice == l_game[0] and user_choice == 2) or (ai_choice == l_game[1] and user_choice == 's') or (user_choice == 'k' and ai_choice == l_game[2]) :
            ai_point += 1
            print("ai +1")
        else:
            print("Drawwww")
    else:
        print('not correct!!!!!!!')
        
    print("\n", "*"*15, "\n")


if ai_point > user_point:
    print("you lose")
elif ai_point == user_point:
    print("Drawww")
else:
    print("You Win")
    
print(f"your point is {user_point} and ai point is {ai_point} !")