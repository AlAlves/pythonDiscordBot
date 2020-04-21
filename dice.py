import random


def rollDice(number_of_dice, number_of_sides):
    return dice = [
        random.choice(range(1, int(number_of_sides) + 1))
        for _ in range(int(number_of_dice))
    ]

def presentRollingDice(number_of_dice, number_of_sides):
    t = rollDice(number_of_dice, number_of_sides)
    tot = sum(t)

    return "["+', '.join(str(x) for x in dice)+"] : "+str(total)
