import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.root.geometry("400x300")

        self.options = ["Rock", "Paper", "Scissors"]
        self.score = {"Wins": 0, "Losses": 0, "Ties": 0}
        
        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.score_label = tk.Label(root, text=self.get_score_text(), font=("Helvetica", 12))
        self.score_label.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.rock_button = tk.Button(button_frame, text="Rock", command=lambda: self.play("Rock"), width=10, bg="lightblue")
        self.rock_button.pack(side=tk.LEFT, padx=50)

        self.paper_button = tk.Button(button_frame, text="Paper", command=lambda: self.play("Paper"), width=10, bg="lightblue")
        self.paper_button.pack(side=tk.LEFT, padx=50)
        
        self.scissor_button = tk.Button(button_frame, text="Scissors", command=lambda: self.play("Scissors"), width=10, bg="lightblue")
        self.scissor_button.pack(side=tk.LEFT, padx=50)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=20)

    def play(self, user_choice):
        computer_choice = random.choice(self.options)
        result = self.determine_winner(user_choice, computer_choice)

        if result == "You win!":
            self.score["Wins"] += 1
        elif result == "You lose!":
            self.score["Losses"] += 1
        else:
            self.score["Ties"] += 1        

        self.result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}.\n{result}")
        self.score_label.config(text=self.get_score_text())

    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Scissors" and computer == "Paper") or \
             (user == "Paper" and computer == "Rock"):
            return "You win!"
        else:
            return "You lose!"
        
    def get_score_text(self):
        return f"Wins: {self.score['Wins']} | Losses: {self.score['Losses']} | Ties: {self.score['Ties']}"

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
