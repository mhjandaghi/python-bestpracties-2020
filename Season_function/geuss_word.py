from random import choice
# def welcome_message():
#      print(f"Welcome to Game.\nyou shuold guees a word we choiced!\nyou 5 times can guess the goal word.\n\n")

# def guess_word():
#     welcome_message() 
#     i = 5
#     words_list = ["abbas", "ali", "mahdi", "karim", "hadis", "sara"]
#     ai_choice = randint(0,len(words_list))
#     print(f"the list of words: {words_list} Starttt!")
#     while i > 0:
#         user_guess = int(input("enter your guess by number: "))
#         if user_guess == ai_choice:
#             return (f"You win! the word is {words_list[user_guess]}.")
#         else:
#             print(f"You lose! Try again.")
#             i -= 1
#     return words_list[ai_choice]

# # print(guess_word())


def add_input():
    user_input = input("enter your word: ")
    words_list_add = []
    while user_input != "exit":
        words_list_add.append(user_input)
        user_input = input("enter your word: ")
    
    return words_list_add


def get_input(list_of_words):
    while True:
        user_input = input("enter your input: ")
        if user_input.lower() in list_of_words:
            return user_input
        print("Try Again! \n")



def help_game():
    print("*" * 10)
    print("welome to the game.")
    print("All word is", words_list)
    print("Start")
    print("*" * 10)



def run_game(number_of_times, list_word_game):
    help_game()
    print(f"{number_of_times} times for guessing.")
    correct_word = choice(list_word_game)
    for guess in range(number_of_times):
        user_input = get_input(list_word_game)
        if user_input == correct_word:
            print("You won!")
            return
        else:
            print(f"your guess is wrong!\nTry again...\n{number_of_times - 1 - guess} left.")
            print("-" * 13)
    print(f"the correct word is {correct_word}\nSorry you lose:(((")

def number_round():
    user_guess = int(input("enter your round by number: "))
    return user_guess


words_list = add_input()

round_of_user = number_round()

run_game(round_of_user, words_list)
