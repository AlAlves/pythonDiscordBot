import random

def testDice(number_of_dice, number_of_sides):
    dice = [
        random.choice(range(1, number_of_sides + 1))
        for _ in range(number_of_dice)
    ]
    total = sum(dice)
    print(', '.join(str(x) for x in dice)+" = "+str(total))
    return 0

# testDice(3,6)
