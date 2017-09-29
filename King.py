from Piece import *

class King(Piece):
    """
    Classe Man, héritant de la classe Piece
    """
    def atomic_moves(self,board):
        """
        Fonction permettant de créer une liste des déplacements possibles pour un pion King

        :param board: plateau de jeu
        :return: une liste de déplacements possibles
        """
        list = []

        x=self.position[0]
        y=self.position[1]
        x_1=self.position[0]-1
        x_2=self.position[0]+1
        y_1=self.position[1]-1
        y_2=self.position[1]+1
        ok_1=0
        ok_2=0
        ok_3=0
        ok_4=0
        while x_1>=0 or x_2<len(board) or y_1>=0 or y_2<len(board):

            if ok_1==0 and x_1>=0 and y_1>=0:
                if board[x_1][y_1] == '_':
                    list+=x,y,x_1,y_1
                else:
                    ok_1=1
            if ok_2==0 and x_1>=0 and y_2<len(board):
                if board[x_1][y_2] == '_':
                    list+=x,y,x_1,y_2
                else:
                    ok_2=1
            if ok_3==0 and x_2<len(board) and y_1>=0:
                if board[x_2][y_1] == '_':
                    list+=x,y,x_2,y_1
                else:
                    ok_3=1
            if ok_4==0 and x_2<len(board) and y_2<len(board):
                if board[x_2][y_2] == '_':
                    list+=x,y,x_2,y_2
                else:
                    ok_4=1

            x_1-=1
            x_2+=1
            y_1-=1
            y_2+=1

        return list

    def atomic_capture(self,board):
        """
        Fonction permettant de créer une liste des captures possibles pour un pion King

        :param board: plateau de jeu
        :return: une liste de captures possible
        """

        list = []
        color_e=''
        color_e_2=''
        if self.color=='K':
            color_e='Q'
            color_e_2='N'
        else :
            color_e='K'
            color_e_2='B'

        x=self.position[0]
        y=self.position[1]
        x_1=self.position[0]-1
        x_2=self.position[0]+1
        y_1=self.position[1]-1
        y_2=self.position[1]+1

        ok_1=0
        ok_2=0
        ok_3=0
        ok_4=0
        while x_1-1>=0 or x_2+1<len(board) or y_1-1>=0 or y_2+1<len(board):

            if ok_1==0 and x_1>=0 and y_1>=0 and x_1-1>=0 and y_1-1>=0:
                if not board[x_1][y_1] == '_':
                    if (board[x_1][y_1].get_color() == color_e or board[x_1][y_1].get_color() == color_e_2) and board[x_1-1][y_1-1] == '_' :
                        list+=self.position[0],self.position[1],x_1,y_1,x_1-1,y_1-1
                    else:
                        ok_1 = 1
            if ok_2==0 and x_1>=0 and y_2<len(board) and  x_1-1>=0 and y_2+1<len(board):
                if not board[x_1][y_2] == '_':
                    if (board[x_1][y_2].get_color() == color_e or board[x_1][y_2].get_color() == color_e_2) and board[x_1-1][y_2+1] == '_' :
                        list+=self.position[0],self.position[1],x_1,y_2,x_1-1,y_2+1
                    else:
                        ok_2=1
            if ok_3==0 and x_2<len(board) and y_1>=0 and x_2+1<len(board) and y_1-1>=0:
                if not board[x_2][y_1] == '_':
                    if (board[x_2][y_1].get_color() == color_e or board[x_2][y_1].get_color() == color_e_2) and board[x_2+1][y_1-1] == '_' :
                        list+=self.position[0],self.position[1],x_2,y_1,x_2+1,y_1-1
                    else:
                        ok_3=1
            if ok_4==0 and x_2<len(board) and y_2<len(board) and x_2+1<len(board) and y_2+1<len(board):
                if not board[x_2][y_2] == '_':
                    if (board[x_2][y_2].get_color() == color_e or board[x_2][y_2].get_color() == color_e_2) and board[x_2+1][y_2+1] == '_' :
                        list+=self.position[0],self.position[1],x_2,y_2,x_2+1,y_2+1
                    else:
                        ok_4=1

            x_1-=1
            x_2+=1
            y_1-=1
            y_2+=1

        return list
