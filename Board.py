from Piece import *
from AtomicMove import *

class Board:
    def __init__(self, size):
        self.size=size
        self.play_board=[['.' for i in range(size)] for j in range(size)]

        for i in range(0,self.size,2):
            for j in range(0,self.size,2):
                self.play_board[i][j]='_'

        for i in range(1,self.size,2):
            for j in range(1,self.size,2):
                self.play_board[i][j]='_'

        for i in range(0,self.size//2-1,2):
            for j in range(0,self.size,2):
                self.play_board[i][j]=Piece((i,j),'B')

        for i in range(1,self.size//2-1,2):
            for j in range(1,self.size,2):
                self.play_board[i][j]=Piece((i,j),'B')

        if self.size//2 %2:
            x=0
            y=1
        else:
            x=1
            y=0

        for i in range(self.size//2+1,self.size,2):
            for j in range(x,self.size,2):
                self.play_board[i][j]=Piece((i,j),'N')

        for i in range(self.size//2+2,self.size,2):
            for j in range(y,self.size,2):
                self.play_board[i][j]=Piece((i,j),'N')


    def to_lines(self):
        print('Voici votre plateau de jeu : \n')
        print('   ', end='')
        for i in range(self.size):
            print('', i, '', end='')
        print()
        for i in range(self.size):
            print(i,'[', end='')
            for j in range(self.size):
                if self.play_board[i][j]== '.' or self.play_board[i][j]== '_' :
                    print('',self.play_board[i][j],'', end='')
                else:
                    print('', self.play_board[i][j].get_color(), '', end='')
            print(']')
        print()
        return



    def move_piece(self):
        x=int(input('Choisir votre pion - Saisir la coordonnée de la ligne : '))
        y=int(input('Choisir votre pion - Saisir la coordonnée de la colonne : '))



        return


    def possible_move(self,player):
        list = []
        print('\nListe des cases accessibles :')
        for x in range(self.size):
            for y in range(self.size):
                if not self.play_board[x][y]== '.' and not self.play_board[x][y]== '_':
                    if player==True and self.play_board[x][y].get_color()=='B':
                        list += self.play_board[x][y].atomic_moves(self.play_board)
                    if player==False and self.play_board[x][y].get_color()=='N':
                        list += self.play_board[x][y].atomic_moves(self.play_board)

        return list