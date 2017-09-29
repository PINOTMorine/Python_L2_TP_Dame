from Man import *
from King import *

class Board:
    """
    Classe Board
    """

    def __init__(self, size):
        """
        Constructeur du plateau de jeu
        Initialisation du plateau

        :param size: taille du plateau
        """
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
                self.play_board[i][j]=Man((i,j),'B')

        for i in range(1,self.size//2-1,2):
            for j in range(1,self.size,2):
                self.play_board[i][j]=Man((i,j),'B')

        if self.size//2 %2:
            x=0
            y=1
        else:
            x=1
            y=0

        for i in range(self.size//2+1,self.size,2):
            for j in range(x,self.size,2):
                self.play_board[i][j]=Man((i,j),'N')

        for i in range(self.size//2+2,self.size,2):
            for j in range(y,self.size,2):
                self.play_board[i][j]=Man((i,j),'N')

    def to_lines(self):
        """
        Affichage du plateau

        :return:
        """
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

    def count_piece(self,color):
        """
        Compte le mondre de pions sur le terrain pour un joueur

        :param color: couleur de pions du joueur
        :return: le nombre de pions
        """
        compteur=0
        for i in range(self.size):
            for j in range(self.size):
                if self.play_board[i][j] is not '_' and self.play_board[i][j] is not '.':
                    if self.play_board[i][j].get_color()==color:
                        compteur+=1
        return compteur

    def possible_move(self,player):
        """
        Créer une liste des déplacements possibles pour un joueur

        :param player: booléen du joueur (True pour le joueur 1 - False pour le joueur 2)
        :return: la liste des déplacements possibles
        """
        list = []
        for x in range(self.size):
            for y in range(self.size):
                if not self.play_board[x][y]== '.' and not self.play_board[x][y]== '_':
                    if player==True and (self.play_board[x][y].get_color()=='B' or self.play_board[x][y].get_color()=='K'):
                        list += self.play_board[x][y].atomic_moves(self.play_board)
                    if player==False and (self.play_board[x][y].get_color()=='N' or self.play_board[x][y].get_color()=='Q'):
                        list += self.play_board[x][y].atomic_moves(self.play_board)

        return list

    def possible_capture(self,player):
        """
        Créer une liste des captures possibles pour un joueur

        :param player: booléen du joueur (True pour le joueur 1 - False pour le joueur 2)
        :return: la liste des captures possibles
        """
        list = []
        for x in range(self.size):
            for y in range(self.size):
                if not self.play_board[x][y]== '.' and not self.play_board[x][y]== '_':
                    if player==True and (self.play_board[x][y].get_color()=='B' or self.play_board[x][y].get_color()=='K'):
                        list += self.play_board[x][y].atomic_capture(self.play_board)
                    if player==False and (self.play_board[x][y].get_color()=='N' or self.play_board[x][y].get_color()=='Q'):
                        list += self.play_board[x][y].atomic_capture(self.play_board)

        return list

    def deplacement_piece(self,num,list,list2):
        """
        Fonction permettant la gestion du déplacement d'une pièce

        :param num: numéro saisi par le joueur, index du déplacement choisi
        :param list: liste des déplacements possibles
        :param list2: liste des captures possibles
        :return:
        """

        j=0
        color=''
        x_start=0
        y_start=0
        x_end=0
        y_end=0
        for i in range(0,len(list),4):
            j+=1
            if j==num:
                x_start=list[i]
                y_start=list[i + 1]
                x_end=list[i + 2]
                y_end=list[i + 3]
        for i in range(0,len(list2),6):
            j+=1
            if j==num:
                x_start=list2[i]
                y_start=list2[i + 1]
                x_capture=list2[i+2]
                y_capture=list2[i+3]
                x_end=list2[i + 4]
                y_end=list2[i + 5]
                color=self.play_board[x_capture][y_capture].get_color()
                self.play_board[x_capture][y_capture]='_'
        self.play_board[x_start][y_start].set_position(x_end,y_end)
        self.play_board[x_end][y_end]=self.play_board[x_start][y_start]
        self.play_board[x_start][y_start]='_'

        # test : if King
        for i in range(self.size):
            for j in range(self.size):
                if not self.play_board[i][j] == '.' and not self.play_board[i][j] == '_':
                    if self.play_board[i][j].get_color()=='B' and i==len(self.play_board)-1:
                        self.play_board[i][j]=King((i,j),'K')
                    elif self.play_board[i][j].get_color()=='N' and i==0:
                        self.play_board[i][j]=King((i,j),'Q')


        return color