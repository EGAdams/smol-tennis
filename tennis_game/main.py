```python
from player import Player
from scoreboard import Scoreboard
from remote import Remote

# Initialize game state
game_state = {
    "player1_score": 0,
    "player2_score": 0,
    "history": []
}

# Create players
player1 = Player("Player 1")
player2 = Player("Player 2")

# Create scoreboard
scoreboard = Scoreboard(game_state, player1, player2)

# Create remotes
player1_remote = Remote(player1, scoreboard)
player2_remote = Remote(player2, scoreboard)

# Game loop
while True:
    # Update scoreboard
    scoreboard.update_scoreboard()

    # Player 1's turn
    print("Player 1's turn")
    player1_remote.press_button()

    # Update scoreboard
    scoreboard.update_scoreboard()

    # Player 2's turn
    print("Player 2's turn")
    player2_remote.press_button()

    # Check if game is over
    if scoreboard.check_game_over():
        print("Game Over!")
        break
```