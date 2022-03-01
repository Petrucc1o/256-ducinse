
#-> 1d20+4+3d2
#-> 1d20 3d2 4
#-> 1 20 3 2 4
#->
#  
from diceroll import diceroll

msg = '1d20+3+1d10'
dice = []
val = []
resultdice = 0
resultval = 0

if 'd' in msg:

    if '+' in msg:
        msg = msg.split('+')

    for c in range(len(msg)):
        if 'd' in msg[c]:
            dice.append(msg[c])
        else:
            val.append(msg[c])

    print('msg:', msg)
    print('dice:', dice)
    print('val:', val)

    for c in range(len(dice)):
        print(dice[c])

        sdice = dice[c].split('d')
        print(sdice)

        resultdice = resultdice + diceroll(int(sdice[0]), int(sdice[1]))
    print(resultdice)

    for c in range(len(val)):
        resultval = int(val[c]) + resultval

    print(resultdice+resultval)

    



    