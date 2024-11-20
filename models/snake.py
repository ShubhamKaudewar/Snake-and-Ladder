
class Snake:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_player_position(self, player):
        print(f"{player.name} has been eaten by 🐍 at {self.start} and moved to {self.end}")
        return self.end