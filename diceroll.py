from random import randint

def diceroll(x, y):
    total = 0
    val = 0
    for c in range(x):
        val = randint(1, y)
        total =+ val
    return(total)