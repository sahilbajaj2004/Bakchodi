import random

def print_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_win(board, player):
    win_combos = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_draw(board):
    return " " not in board

def player_move(board):
    while True:
        try:
            move = int(input("Your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Spot already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Enter number 1-9.")

def computer_move(board):
    available = [i for i, spot in enumerate(board) if spot == " "]
    move = random.choice(available)
    board[move] = "O"
    print(f"Computer chose position {move + 1}")

def play_game():
    board = [" "] * 9
    print("You are X, computer is O.")
    print("Board positions:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    while True:
        print_board(board)
        player_move(board)
        if check_win(board, "X"):
            print_board(board)
            print("🎉 You win!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        computer_move(board)
        if check_win(board, "O"):
            print_board(board)
            print("😔 Computer wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

# Run the game
play_game()
