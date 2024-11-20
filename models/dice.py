from service.dice_roll_strategy import DiceRollStrategy

class Dice:
    def __init__(self, strategy="default"):
        self.strategy = strategy

    def roll(self):
        return DiceRollStrategy().roll(strategy=self.strategy)