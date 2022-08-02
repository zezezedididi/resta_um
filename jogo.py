import numpy as np

class Jogo:
    def __init__(self):
        self.tabuleiro = np.zeros((7,7))
        self.tabuleiro[:2,:2]= -1
        self.tabuleiro[:-2,:2]= -1
        self.tabuleiro[:2,:-2]= -1
        self.tabuleiro[:-2,:-2]= -1

    def play (self,position,play):
        p0=position[0]
        p1=position[1]
        pl0=play[1]
        pl1=play[2]

        if(p0<0 or p1<0 or p0>6 or p1>6):#if position exists
            print('invalid position something went wrong')
            return -1

        if(p0+pl0<0 or p0+pl0>6 or p1+pl1<0 or p1+pl1>6):#play out of bounds
            print('play out of bounds,something went wrong!')
            return -1

        if(p0+pl0*2<0 or p0+pl0*2>6 or p1+pl1*2<0 or p1+pl1*2>6):#play out of bounds
            print('end position out of bounds,something went wrong!')
            return -1

        if(self.tabuleiro[p1,p2]!=1):# ball in position
            print('ball not in position!')
            return -1

        if(self.tabuleiro[p0+pl0,p1+pl1]!=1):
            print('there s no ball to jump')
            return -1

        if(self.tabuleiro[p0+pl0*2,p1+pl1*2]!=1):
            print('end position isnt empty')
            return -1

        self.tabuleiro[p0,p1]=0
        self.tabuleiro[p0+pl0,p1+pl1]=0
        self.tabuleiro[p0+pl0*2,p1+pl1*2]=1


if __name__ == '__main__':
    jogo = Jogo()
    print(jogo.tabuleiro[1,1])
