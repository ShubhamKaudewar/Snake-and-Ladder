from models.dice import Dice
from models.player import Player
from models.board import Board

class SnakeAndLadderGame:
    def __init__(self, ladders, snakes, players, strategy="default"):
        self.players = players
        self.dice = Dice(strategy=strategy)
        self.player = Player
        self.board = Board(ladders, snakes)

    def start_game(self):
        win_score, total_players = 1, len(self.players)
        while win_score != 4:
            for player in self.players:
                if player.won:
                    continue
                rolled = self.dice.roll()
                print(f"\n{player.name} is at {player.position} and rolling the dice..."
                      f"\n{player.name} rolled: {rolled}")
                player.move(rolled, self.board)
                self.board.check_coordinate_status(player)

                if player.is_winner():
                    print(f"Congratulations 🎉🎉 {player.name} you came {win_score}!")
                    player.won = win_score
                    print(f"Player remaining {total_players - win_score}!")
                    win_score += 1

        print("\n\nLeaderBoard 🗒️")
        for player in self.players:
            print(f"{player.name} has came {player.won} and total dice rolled: {player.attempt}")