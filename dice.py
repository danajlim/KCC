from collections import Counter
import random
class Dice:
    def __init__(self):
        self.number = 0

    def roll(self): 
        self.number = random.randint(1,6)
        return(self.number)

class DiceProbability():
    
    def __init__(self, n):
        self.total=n
        self.a=[]*n
        self.b=[0,0,0,0,0,0]

    def calcProbability(self, n):
        i=0
        while i<n:
            self.a.append(Dice().roll())
            i=i+1

        i=0
        while i<6:
            self.b[i]=self.a.count(i+1)/self.total
            i=i+1

    def printProbability(self, n):
        print('총횟수:'+str(n)+'번')
        i=0
        while i<6:
            print('주사위'+str(i+1)+':'+str(self.b[i]*n)+'번   비율:'+str(self.b[i]))
            i=i+1