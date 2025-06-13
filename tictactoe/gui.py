import tkinter as tk
import random
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe - You vs Computer")

# Game board state
board = [" " for _ in range(9)]
buttons = []

# Check for win
def check_win(player):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# Check for draw
def check_draw():
    return " " not in board

# Computer move
def computer_move():
    available = [i for i, val in enumerate(board) if val == " "]
    if not available:
        return
    move = random.choice(available)
    board[move] = "O"
    buttons[move].config(text="O", state="disabled", disabledforeground="red")

    if check_win("O"):
        messagebox.showinfo("Game Over", "😔 Computer Wins!")
        reset_board()
    elif check_draw():
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset_board()

# Player move (on button click)
def player_move(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i].config(text="X", state="disabled", disabledforeground="green")

        if check_win("X"):
            messagebox.showinfo("Game Over", "🎉 You Win!")
            reset_board()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_board()
        else:
            root.after(500, computer_move)

# Reset game
def reset_board():
    global board
    board = [" " for _ in range(9)]
    for btn in buttons:
        btn.config(text=" ", state="normal")

# Create GUI buttons
for i in range(9):
    btn = tk.Button(root, text=" ", font=("Helvetica", 24), width=5, height=2,
                    command=lambda i=i: player_move(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Run the GUI loop
root.mainloop()
