import random

class DiceRollStrategy:
    def roll(self, strategy="default"):
        if strategy in ["default", "fair"]:
            return FairDiceRollStrategy().roll()
        elif strategy == "crooked":
            return CrookedDiceRollStrategy().roll()
        else:
            raise ValueError(f"Strategy {strategy} not recognized")

class FairDiceRollStrategy(DiceRollStrategy):
    def roll(self):
        return random.randint(1, 6)

class CrookedDiceRollStrategy(DiceRollStrategy):
    def roll(self):
        p = random.random()
        if p < 0.2:
            return random.choice([1, 3, 5])
        return random.randint(1, 3) * 2

