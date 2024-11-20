

class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_player_position(self, player):
        print(f"{player.name} had climbed 🪜 from {self.start} to {self.end}")
        return self.end
