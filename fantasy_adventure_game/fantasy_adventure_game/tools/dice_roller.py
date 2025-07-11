import random

def roll_dice(sides=6, rolls=1):
    return [random.randint(1, sides) for _ in range(rolls)]