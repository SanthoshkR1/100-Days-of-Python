import tkinter as tk
from tkinter import messagebox

# Global variables to track the current player and winner
current_player = "X"
winner = False

# Function to check for a winner
def check_winner():
    global winner           
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != "":
            buttons[combo[0]].config(bg="red")
            buttons[combo[1]].config(bg="red")
            buttons[combo[2]].config(bg="red")
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True  # Set the winner flag
            root.quit()  # Close the game window

# Function to handle button click
def button_click(indx):
    global current_player, winner
    if buttons[indx]['text'] == "" and not winner:  # Only allow moves if the button is empty and there's no winner
        buttons[indx]['text'] = current_player  # Set the text on the button to the current player
        check_winner()  # Check for a winner after the move
        toggle_player()  # Switch to the next player

# Function to switch players
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Create the game window and set up the board
root = tk.Tk()
root.title("Tic Tac Toe")

# Create a list of buttons
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

# Arrange the buttons in a grid layout
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Create a label to show whose turn it is
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Start the Tkinter event loop
root.mainloop()