import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(root, text="I'm thinking of a number between 1 and 100.")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.attempts += 1

            if user_guess < self.number_to_guess:
                messagebox.showinfo("Result", "Too low! Try again.")
            elif user_guess > self.number_to_guess:
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number {self.number_to_guess} in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()