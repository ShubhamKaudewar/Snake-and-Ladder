from models.ladder import Ladder
from models.snake import Snake
from models.player import Player
from service.snake_and_ladder_game import SnakeAndLadderGame

def main():
    ladders = {
        1: Ladder(1, 38),
        4: Ladder(4, 14),
        8: Ladder(8, 30),
        21: Ladder(21, 42),
        28: Ladder(28, 76),
        50: Ladder(50, 67),
        71: Ladder(71, 92),
        88: Ladder(88, 99)
    }

    snakes = {
        32: Snake(32, 10),
        36: Snake(36, 6),
        48: Snake(48, 26),
        62: Snake(62, 18),
        88: Snake(88, 24),
        95: Snake(95, 56),
        97: Snake(97, 78)
    }

    n = int(input("Total number of players playing:"))
    players = []
    for i in range(n):
        players.append(Player(name=input(f"\nProvide player name {str(i+1)}")))
    response = input("start the game?[Y/N]")

    # n = 2
    # response = "y"
    # players.append(Player(name="amol"))
    # players.append(Player(name="shubham"))

    if response.lower() == "y":
        print("*** Game started ***")
        SnakeAndLadderGame(ladders, snakes, players).start_game()
    elif response.lower() == "n":
        print("*** Game stopped ***")
    else:
        ValueError(f"Please provide appropriate input Y/N. Input provided:{response}")

if __name__ == "__main__":
    main()
