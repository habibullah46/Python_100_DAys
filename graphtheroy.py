def draw_board(board):
    print("----++---++----")
    for i in range(3):
        for j in range(3):
            print("| ", end="")
            k = i * 3 + j
            if board[k] == 0:
                print(k + 1, "|", end="")
            elif board[k] == -1:
                print("X |", end="")
            else:
                print("O |", end="")
        print("\n----++---++----")


def win(board):1
    # Determines if a player has won, returns 0 otherwise.
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(8):
        if board[wins[i][0]] != 0 and board[wins[i][0]] == board[wins[i][1]] == board[wins[i][2]]:
            return board[wins[i][2]]
    return 0


def minimax(board, player):
    winner = win(board)
    if winner != 0:
        return winner * player

    move = -1
    score = -2

    for i in range(9):
        if board[i] == 0:
            board[i] = player
            this_score = -minimax(board, player * -1)
            if this_score > score:
                score = this_score
                move = i
            board[i] = 0  # Reset board after try

    if move == -1:
        return 0

    return score


def computer_move(board):
    move = -1
    score = -2

    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            temp_score = -minimax(board, -1)
            board[i] = 0
            if temp_score > score:
                score = temp_score
                move = i

    return move


if __name__ == "__main__":
    print("\n~~Tic Tac Toe\n")
    print("\n\n   BOARD:\n")
    print("----++---++----")
    print("| 1 || 2 || 3 |")
    print("----++---++----")
    print("| 4 || 5 || 6 |")
    print("----++---++----")
    print("| 7 || 8 || 9 |")
    print("----++---++----\n\n\n")
    print("Only legal moves are the numbers you see on the board\n\n")

    board = [0] * 9
    moves = 0
    # Player = -1 ; Computer = 1
    while moves < 9:
        mv = int(input("Enter Player 1's Move\n"))
        if board[mv - 1] == 0:
            board[mv - 1] = -1
            moves += 1
            print("\n\nBoard after your move:\n")
            draw_board(board)
            if win(board) == 0:
                k = computer_move(board)
                board[k] = 1
                print("\n\nBoard after computer's move:\n")
                draw_board(board)
                moves += 1
                if win(board) != 0:
                    break
            else:
                break
        else:
            print("Illegal Move, Try again !! \n\n")

    result = win(board)
    if result == 0:
        print("It's a draw. Better Smart next time.\n")
    elif result == 1:
        print("You lose.\n")
    elif result == -1:
        print(
            "This will never Happen. But if it does (It never will), Congratulations, You have beaten the unbeatable\n")
