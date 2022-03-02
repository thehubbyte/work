import random
import math


def create_board(n, jello = True):
    arr = [[0 for row in range(n)] for column in range(n)]

    for i in range(n):
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)
        if arr[x][y] == 1:
            while True:
                x = random.randint(0, n-1)
                y = random.randint(0, n-1)
                if arr[x][y] == 0:
                    arr[x][y] = 1
                    break
                else:
                    continue
        else:
            arr[x][y] = 1
    if jello == True:
        for row in arr:
            print(" ".join(str(cell) for cell in row))
    return arr

def get_user_input(n):
    #issue if 1 number or no number is input = crash
    user_input = input(f"Enter a number where first digit is the rows and 2nd is columns less than {n}:")
    split_input = [int(i) for i in str(user_input)]
    row = split_input[0]
    column = split_input[1]
    while row > (n-1) or column > (n-1):
        print("That number is out of range you FOOL, please try again.")
        user_input = input(f"Enter a number where first digit is the rows and 2nd is columns less than {n}:")
        split_input = [int(i) for i in str(user_input)]
        row = split_input[0]
        column = split_input[1]
    else:
        return split_input

def clear_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = 0



def game():
    bomb_or_nah = False
    n = 4
    cnt = 0
    board = create_board(n)
    user_board = create_board(n, False)
    clear_board(user_board)
    while cnt < ((n * n) - 4):
        # grab user input then check if user input is a bomb
        split_input = get_user_input(n)
        row = split_input[0]
        column = split_input[1]
        if board[row][column] == 1:
            print("BOOM! Game over")
            quit()
        elif board[row][column] == 2:
            print("you have already been there done that, now do it again.")
            bomb_or_nah = True
        else:
            bomb_or_nah = False
            cnt += 1

        if bomb_or_nah == False:
            board[row][column] = 2
            user_board[row][column] = "X"
            print("You have survived this round congratulations, want a cookie?")
            for i in user_board:
                print(" ".join(str(cell) for cell in i))
    print("You have gotten not a single mine and won, that is incredible!!!")












game()
