import tkinter as tk
import random

class OddEvenGame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Odd or Even Game")
        self.pack()
        
        self.create_widgets()

    def create_widgets(self):
        # Add labels to explain the rules of the game
        self.rule1_label = tk.Label(self, text="Guess if the sum of two dice is odd or even.")
        self.rule1_label.pack()

        self.rule2_label = tk.Label(self, text="If you guess correctly, you win!")
        self.rule2_label.pack()

        # Add a label to show the result of the dice roll
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

        # Add a button to roll the dice
        self.roll_button = tk.Button(self, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

        # Add an entry box for the user to make their guess
        self.guess_entry = tk.Entry(self)
        self.guess_entry.pack()

    def roll_dice(self):
        # Roll the dice and calculate the sum
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2

        # Determine if the sum is odd or even
        if total % 2 == 0:
            result = "even"
        else:
            result = "odd"

        # Get the user's guess
        guess = self.guess_entry.get()

        # Display the result
        if guess == result:
            self.result_label.config(text=f"You win! The sum is {total}, which is {result}.")
        else:
            self.result_label.config(text=f"You lose! The sum is {total}, which is {result}.")
root = tk.Tk()

game = OddEvenGame(root)

game.mainloop()

