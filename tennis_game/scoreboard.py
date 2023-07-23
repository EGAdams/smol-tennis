```python
from tkinter import Label, StringVar
from .styles import colors
from .player import Player

class Scoreboard:
    def __init__(self, root):
        self.root = root
        self.scoreboard = Label(self.root, bg=colors['black'], fg=colors['white'])
        self.scoreboard.pack()

        self.player1_score = StringVar()
        self.player2_score = StringVar()

        self.player1 = Player(self.player1_score)
        self.player2 = Player(self.player2_score)

        self.update_scoreboard()

    def update_scoreboard(self):
        self.scoreboard.config(text=f"Player 1: {self.player1.score.get()} - Player 2: {self.player2.score.get()}")

    def update_score(self, player):
        if player == 1:
            self.player1.increment_score()
        else:
            self.player2.increment_score()
        self.update_scoreboard()

    def undo_score(self, player):
        if player == 1:
            self.player1.decrement_score()
        else:
            self.player2.decrement_score()
        self.update_scoreboard()

    def reset_game(self):
        self.player1.reset_score()
        self.player2.reset_score()
        self.update_scoreboard()
```