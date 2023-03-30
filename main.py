import dice

n=int(input('주사위를 몇번 던지시겠습니까?:'))
dice=dice.DiceProbability(n)
dice.calcProbability(dice.total)
dice.printProbability(dice.total)