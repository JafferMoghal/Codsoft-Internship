import tkinter as tk
from tkinter import messagebox
import random

choices = ['Rock', 'Paper', 'Scissors']

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors'):
        return "yay! you win..."
    elif (user_choice == 'paper' and computer_choice == 'rock'):
        return "yay! you win..."
    elif (user_choice == 'scissors' and computer_choice == 'paper'):
        return "yay! you win..."
    else:
        return "You lost! Better luck next time!!"

def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_message = f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}"
    
    messagebox.showinfo("Game Result", result_message)

root = tk.Tk()
root.title("Rock, Paper and Scissiors Game")

root.geometry("400x300")
root.configure(bg='#f0f0f0')

frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(expand=True)

title_label = tk.Label(frame, text="Rock, Paper, Scissors Game", font=("Helvetica", 30, "bold"), bg='#000533',fg='#ffffff')
title_label.pack(pady=20)

styling = {
    "font": ("Helvetica", 16,"bold"),
    "bg": "#004f14",
    "fg": "#ffffff",
    "width": 20,
    "height": 2,
    "bd": 0,
    "relief": "flat"
}

rock_button = tk.Button(frame, text="Rock", command=lambda: play('Rock'), **styling)
rock_button.pack(pady=10)

paper_button = tk.Button(frame, text="Paper", command=lambda: play('Paper'), **styling)
paper_button.pack(pady=10)

scissors_button = tk.Button(frame, text="Scissors", command=lambda: play('Scissors'), **styling)
scissors_button.pack(pady=10)

root.mainloop()

