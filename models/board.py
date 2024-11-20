from models.ladder import Ladder


class Board:
    def __init__(self, Ladders, Snakes, target=100, starting=1):
        self.ladders = Ladders
        self.snakes = Snakes
        self.target = target
        self.starting = starting

    def check_coordinate_status(self, player):
        if player.position in self.ladders:
            player.position = self.ladders[player.position].get_player_position(player)
        elif player.position in self.snakes:
            player.position = self.snakes[player.position].get_player_position(player)
