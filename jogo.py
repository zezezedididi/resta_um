import numpy as np
import matplotlib.pyplot as plt
import copy

ATEMPED_PLAYS = 0

def draw_game(g: np.ndarray, ax: plt.Axes):
    ax.cla()
    ax.matshow(g, vmin=-1, vmax=1)
    plt.pause(1)

class Jogo:
    def __init__(self):
        self.tabuleiro = np.ones((7,7))
        self.reset()

    def reset(self):
        self.tabuleiro[:,:] = 1
        self.tabuleiro[:2,:2]= -1
        self.tabuleiro[:2,-2:]= -1
        self.tabuleiro[-2:,:2]= -1
        self.tabuleiro[-2:,-2:]= -1
        self.tabuleiro[3,3]=0

    def get_marbles(self):
        counter=0
        for i, row in enumerate(jogo.tabuleiro):
            for j, position in enumerate(row):
                position = (i, j)
                if jogo.tabuleiro[position] ==1:
                    counter = counter+1

        return counter

    def play (self,position,play):
        p0=position[0]
        p1=position[1]
        pl0=play[0]
        pl1=play[1]

        global ATEMPED_PLAYS
        ATEMPED_PLAYS = ATEMPED_PLAYS + 1

        #as coisas comentadas têm haver com nao serem necessarios esse checks

        #if(p0<0 or p1<0 or p0>6 or p1>6):#if position exists
        #    print('invalid position something went wrong')
        #    return -1

        #if(p0+pl0<0 or p0+pl0>6 or p1+pl1<0 or p1+pl1>6):#play out of bounds
        #    print('play out of bounds,something went wrong!')
        #    return -1

        #if(p0+pl0*2<0 or p0+pl0*2>6 or p1+pl1*2<0 or p1+pl1*2>6):#play out of bounds
        #    print('end position out of bounds,something went wrong!')
        #    return -1

        #if(self.tabuleiro[p0,p1]!=1):# ball in position
        #    print('ball not in position!')
        #    return -1

        #if(self.tabuleiro[p0+pl0,p1+pl1]!=1):
        #    print('there s no ball to jump')
        #    return -1

        #if(self.tabuleiro[p0+pl0*2,p1+pl1*2]!=0):
        #    print('end position isnt empty')
        #    return -1

        self.tabuleiro[p0,p1]=0
        self.tabuleiro[p0+pl0,p1+pl1]=0
        self.tabuleiro[p0+pl0*2,p1+pl1*2]=1

    def __str__(self):
        return f"{self.tabuleiro}"

    def revert(self,position,play):
        p0=position[0]
        p1=position[1]
        pl0=play[0]
        pl1=play[1]

        if(p0<0 or p1<0 or p0>6 or p1>6):#if position exists
            print('invalid position something went wrong')
            return -1

        if(p0+pl0<0 or p0+pl0>6 or p1+pl1<0 or p1+pl1>6):#play out of bounds
            print('play out of bounds,something went wrong!')
            return -1

        if(p0+pl0*2<0 or p0+pl0*2>6 or p1+pl1*2<0 or p1+pl1*2>6):#play out of bounds
            print('end position out of bounds,something went wrong!')
            return -1

        if(self.tabuleiro[p0,p1]!=0):# ball in position
            print('ball not in position!')
            return -1

        if(self.tabuleiro[p0+pl0,p1+pl1]!=0):
            print('there s no ball to jump')
            return -1

        if(self.tabuleiro[p0+pl0*2,p1+pl1*2]!=1):
            print('end position isnt empty')
            return -1

        self.tabuleiro[p0,p1]=1
        self.tabuleiro[p0+pl0,p1+pl1]=1
        self.tabuleiro[p0+pl0*2,p1+pl1*2]=0

class Solver:
    def __init__(self):
        #self.marbles_left=self.get_marbles(jogo.tabuleiro)
        self.movents = []
        #self.directions = [[0,1],[1,1],[1,0],[0,-1],[-1,-1],[-1,0],[1,-1],[-1,1]] #inclui diagonais
        self.directions = [[0,1],[1,0],[-1,0],[0,-1]] # puramente cartasiano
        self.winning_moves= [None]*Jogo().get_marbles()
        self.dictionary = {}

    def solve(self,jogo,ax,depth):
        #marbles=jogo.get_marbles()
        print(f"{depth=}, {ATEMPED_PLAYS=}")

        key = jogo.tabuleiro.tobytes()
        if key in self.dictionary:
            #print('trash')
            return 0
        self.dictionary[key] = 1

        if depth == 0:
            if(jogo.tabuleiro[3][3]==1):
                return 1
            else:
                return 0
        plays = self.get_plays(jogo)
        for play in plays:
            jogo2 = copy.deepcopy(jogo)
            jogo2.play(*play)

            if (self.solve(jogo2,ax,depth-1)) == 1 :
                self.winning_moves[depth-1] = play
                return 1
        return 0

    def get_plays(self,jogo):
        movement=[]
        for i, row in enumerate(jogo.tabuleiro):
            for j, position in enumerate(row):
                position = [i, j]
                if jogo.tabuleiro[i, j] == 1:
                    for play in self.directions:
                        if (self.possible_play(jogo.tabuleiro, position, play) == 1):
                            movement.append([position, play])
        return movement

    def possible_play(self, tabuleiro,position,play):
        p0=position[0]
        p1=position[1]
        pl0=play[0]
        pl1=play[1]

        #if(p0<0 or p1<0 or p0>6 or p1>6):#if position exists
        #   print('invalid position something went wrong')
        #   return -1

        if(p0+pl0<0 or p0+pl0>6 or p1+pl1<0 or p1+pl1>6):#play out of bounds
            #print('play out of bounds,something went wrong!')
            return -1

        if(p0+pl0*2<0 or p0+pl0*2>6 or p1+pl1*2<0 or p1+pl1*2>6):#play out of bounds
            #print('end position out of bounds,something went wrong!')
            return -1

        #if(tabuleiro[p0,p1]!=1):# ball in position
            #print('ball not in position!')
        #   return -1

        if(tabuleiro[p0+pl0,p1+pl1]!=1):
            #print('there s no ball to jump')
            return -1

        if(tabuleiro[p0+pl0*2,p1+pl1*2]!=0):
            #print('end position isnt empty')
            return -1

        return 1




if __name__ == '__main__':
    import pickle
    jogo = Jogo()
    fig, ax = plt.subplots()

    draw_game(jogo.tabuleiro, ax)

    solver = Solver()

    marbles=jogo.get_marbles()
    solver.winning_moves=[None]*(marbles-1)
    solver.solve(jogo,ax,marbles-1)

    solver.winning_moves.reverse()

    with open("data.pkl", "wb") as f:
        pickle.dump(solver.winning_moves, f)
    print("Winning moves:")
    print(solver.winning_moves)


    #com diagonais
    #solver.winning_moves=[[[1, 3], [1, 0]], [[2, 1], [0, 1]], [[0, 2], [1, 0]], [[0, 4], [0, -1]], [[2, 3], [0, -1]], [[2, 0], [0, 1]], [[2, 4], [-1, 0]], [[2, 6], [0, -1]], [[3, 1], [-1, 1]], [[0, 4], [1, -1]], [[3, 2], [-1, 0]], [[0, 2], [1, 0]], [[3, 4], [0, -1]], [[3, 2], [-1, 0]], [[3, 5], [-1, -1]], [[4, 0], [-1, 0]], [[5, 2], [-1, 0]], [[4, 3], [-1, -1]], [[2, 0], [0, 1]], [[1, 2], [1, 0]], [[5, 4], [-1, 0]], [[3, 6], [1, -1]], [[6, 3], [-1, 1]], [[4, 6], [0, -1]], [[6, 4], [-1, -1]], [[3, 2], [1, 0]], [[6, 2], [-1, 0]], [[4, 1], [0, 1]], [[4, 3], [0, 1]], [[4, 5], [-1, -1]], [[1, 3], [1, 0]]]

    #sem diagonais
    #solver.winning_moves=[[[1, 3], [1, 0]], [[2, 1], [0, 1]], [[0, 2], [1, 0]], [[0, 4], [0, -1]], [[2, 3], [0, -1]], [[2, 0], [0, 1]], [[2, 4], [-1, 0]], [[2, 6], [0, -1]], [[3, 2], [-1, 0]], [[0, 2], [1, 0]], [[3, 0], [0, 1]], [[3, 2], [-1, 0]], [[3, 4], [-1, 0]], [[0, 4], [1, 0]], [[3, 6], [0, -1]], [[3, 4], [-1, 0]], [[5, 2], [-1, 0]], [[4, 0], [0, 1]], [[4, 2], [-1, 0]], [[1, 2], [1, 0]], [[3, 2], [0, 1]], [[4, 4], [-1, 0]], [[1, 4], [1, 0]], [[4, 6], [0, -1]], [[4, 3], [0, 1]], [[6, 4], [-1, 0]], [[3, 4], [1, 0]], [[6, 2], [0, 1]], [[6, 4], [-1, 0]], [[4, 5], [0, -1]], [[5, 3], [-1, 0]]]


    jogo.reset()
    for move in solver.winning_moves:
        jogo.play(*move)
        draw_game(jogo.tabuleiro, ax)

#    exit = True
#    while exit :
#        entry=input("enter marble:\n")
#        if entry == "x":
#            exit=False
#        p0,p1 = entry.split()
#        position = [int(p0),int(p1)]# getting the marble
#
#        draw_game(jogo.tabuleiro, ax)# drawing
#        plt.pause(1)
#
#        temp = jogo.tabuleiro[int(p0),int(p1)]
#        print(temp)
#        jogo.tabuleiro[int(p0),int(p1)] = -1
#        print(jogo.tabuleiro)
#
#        draw_game(jogo.tabuleiro, ax)# draw
#        plt.pause(1)
#
#        jogo.tabuleiro[int(p0),int(p1)] = temp
#
#        draw_game(jogo.tabuleiro, ax)# draw
#        plt.pause(1)
#
#        entry = input ("enter play:\n")
#        if entry == "x":
#            exit=False
#        p0,p1 = entry.split()
#        print(p0,p1)
#        play = (int(p0),int(p1))# getting the play
#
#        jogo.play(position,play)
#
#        draw_game(jogo.tabuleiro, ax)# draw
#        plt.pause(1)
