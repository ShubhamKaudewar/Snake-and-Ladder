
class Player:
    def __init__(self, name, position=0, won=0):
        self.name = name
        self.position = position
        self.attempt = 0
        self.won = won

    def move(self, rolled, board):
        self.attempt += 1
        next_position = self.position + rolled
        if next_position > board.target:
            required = board.target - self.position
            print(f"Try again you required:{required}")
        else:
            self.position = next_position
            print(f"{self.name} moved to {self.position}")

    def is_winner(self):
        if self.position == 100:
            return True
        return False