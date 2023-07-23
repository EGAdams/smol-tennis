```python
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.score_history = []

    def update_score(self):
        self.score_history.append(self.score)
        self.score += 1

    def undo_score(self):
        if self.score_history:
            self.score = self.score_history.pop()
        else:
            print("No previous score to undo.")

    def reset_game(self):
        self.score = 0
        self.score_history = []
```