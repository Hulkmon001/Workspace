import random
import tkinter as tk

# define the possible choices for the game
choices = ["rock", "paper", "scissors", "suicide"]

# function to handle the user's choice
def choose(option):
    # randomly select the computer's choice
    computer_choice = random.choice(choices)

    # display the choices made by the user and the computer
    user_label.configure(text="You chose: " + option)
    computer_label.configure(text="Computer chose: " + computer_choice)

    # determine the winner of the game
    if option == computer_choice:
        result_label.configure(text="It's a tie!")
    elif option == "rock" and computer_choice == "scissors" or \
         option == "paper" and computer_choice == "rock" or \
         option == "scissors" and computer_choice == "paper":
        result_label.configure(text="You win!")
    else:
        result_label.configure(text="Computer wins!")

# create the GUI window
window = tk.Tk()
window.title("Rock, Paper, Scissors, Suicide")

# create the user interface elements
title_label = tk.Label(window, text="Choose rock, paper, scissors, or suicide:")
title_label.pack()

rock_button = tk.Button(window, text="Rock", command=lambda: choose("rock"))
rock_button.pack()

paper_button = tk.Button(window, text="Paper", command=lambda: choose("paper"))
paper_button.pack()

scissors_button = tk.Button(window, text="Scissors", command=lambda: choose("scissors"))
scissors_button.pack()

suicide_button = tk.Button(window, text="Suicide", command=lambda: choose("suicide"))
suicide_button.pack()

user_label = tk.Label(window, text="")
user_label.pack()

computer_label = tk.Label(window, text="")
computer_label.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# start the GUI event loop
window.mainloop()
