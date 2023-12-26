from termcolor import colored
from time import sleep
from os import system

winners = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
moves = ((1,3,7,9), (5,), (2,4,6,8))
board = list(range(1, 10))
player, computer = "X", "O"

def print_board():
    j = 1
    for i in board:
        end_line = "  "
        if j % 3 == 0:
            end_line = "\n\n"
        if i == "X":
            print(colored(f"[{i}]", "red"), end= end_line)
        elif i == "O":
            print(colored(f"[{i}]", "yellow"), end= end_line)
        else:
            print(colored(f"[{i}]", "green"), end= end_line)
        j += 1



def has_empty_space():
    return board.count("X") + board.count("O") != len(board)


print(f"\nplayer is {player}\nai is {computer}!\n")


def choice_player():
    user_choice = int(input("enter your move: "))
    print()
    return user_choice


def can_move(b, m):
    if m in board and isinstance(b[m - 1], int):
        return True
    return False


def is_winner(brd, ply):
    win = True
    for tup in winners:
        win = True
        for j in tup:
            if brd[j] != ply:
                win = False
                break
        if win:
            break
    return win


def make_move(b, p, m, undo = False):
    if can_move(b, m):
        b[m - 1] = p
        win = is_winner(b, p)
        if undo:
            b[m - 1] = m
        return True, win
    return False, False



def computer_move():
    mv = -1
    sleep(0.65)
    # ایا خودش برنده میشه؟؟
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break

    # جلوگیری از برنده شدن کاربر       
    if mv == -1:
        for m in range(1, 10):
            if make_move(board, player, m, True)[1]:
                mv = m
                break

    # حرکت هوشمندانه
    if mv == -1:
        for tup in moves:
            for j in tup:
                if mv == -1 and can_move(board, j):
                    mv = j
                    break

    return make_move(board, computer, mv)

    


while has_empty_space():
    print_board()
    
    move_player = choice_player()
    moved, won = make_move(board, player, move_player)

    if not moved:
        print("Invalid... Try again!!")
        continue
    if won:
        print(colored("You Won!", "green"),"\n")
        print_board()
        break
    elif computer_move()[1]:
        print(colored("You lose!", "yellow"),"\n")
        print_board()
        break
    
    system("cls")