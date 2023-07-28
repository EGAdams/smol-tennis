```python
from button import Button
from player import Player

class Remote:
    def __init__(self, player):
        self.player = player
        self.score_button = Button('SCORE', self.player.update_score)
        self.undo_button = Button('UNDO', self.player.undo_score)
        self.reset_button = Button('RESET GAME', self.player.reset_game)

    def press_button(self, button_name):
        if button_name == 'SCORE':
            self.score_button.click()
        elif button_name == 'UNDO':
            self.undo_button.click()
        elif button_name == 'RESET GAME':
            self.reset_button.click()
        else:
            print("Invalid button")

# Example usage:
# player1 = Player("Player 1")
# player1_remote = Remote(player1)
# player1_remote.press_button('SCORE')
```