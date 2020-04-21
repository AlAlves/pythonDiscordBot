import random

def rollDice(number_of_dice, number_of_sides):
    return [random.choice(range(1, number_of_sides+1)) for _ in range(number_of_dice)]

def presentRollingDice(number_of_dice, number_of_sides):
    t = rollDice(number_of_dice, number_of_sides)
    total = sum(t)

    return "`["+', '.join(str(x) for x in t)+"] = "+str(total)+"`"
