```python
from enum import Enum

class Button(Enum):
    SCORE = 1
    UNDO = 2
    RESET_GAME = 3

class ButtonAction:
    def __init__(self, button_type):
        self.button_type = button_type

    def press(self):
        if self.button_type == Button.SCORE:
            return "score"
        elif self.button_type == Button.UNDO:
            return "undo"
        elif self.button_type == Button.RESET_GAME:
            return "reset"
        else:
            return "Invalid button"
```