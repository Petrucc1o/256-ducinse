from random import randint

def diceroll(x, y):
    total = 0
    val = 0
    for c in range(x):
        val = randint(1, y)
        total =+ val
    return(total)

# msg = ['1d20+1d10', '1d20+8', '1d20+1d10', '1d20+1d10+8', '6+1d20+6', '18d40+1d18+200']
msgfind = ''

dice = {
    'dices': [],
    'number': [],
    'sides': [],
    'result': [],
    'operatordice': [],
    'values': [],
    'operatorval': []
}

def roll(msg):

    dicesp = []
    msg = msg.split('+')

    dice['dices'] = []
    dice['number'] = []
    dice['sides'] = []
    dice['result'] = []
    dice['operatordice'] = []
    dice['values'] = []
    dice['operatorval'] = []

    for c in range(len(msg)):
        if 'd' in msg[c]:
            dice['dices'].append(msg[c])
        else:
            dice['values'].append(int(msg[c]))

    dicesp = []
    for c in range(len(dice['dices'])):
        dicesp = dice['dices'][c].split('d')
        print(dicesp)
        dice['number'].append(dicesp[0])
        dice['sides'].append(dicesp[1])
        dice['result'].append(diceroll(int(dice['number'][c]), int(dice['sides'][c])))


    print('msg:', msg)
    print('dice:', dice)
    print('val:')

    return(dice)


# in a future update will output a nice formated string for printing on the bot
#def assembler(dice):


