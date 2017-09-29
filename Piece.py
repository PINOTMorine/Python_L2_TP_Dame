class Piece:
    """
    Classe Piece
    """

    def __init__(self, position, color):
        """
        Constructeur du plateau de jeu
        Initialisation du plateau

        :param position: list de coordonnées x et y du pion
        :param color: couleur du pion
        """

        self.position=position
        self.color=color

    def get_color(self):
        """
        Retourne la couleur d'un pion

        :return: la lettre de la couleur du pion
        """
        return self.color

    def get_position(self):
        """
        Retourne la position d'un pion

        :return: retourne les coordonnées d'un pion
        """
        return self.position

    def set_position(self,x,y):
        """
        Modifie la position d'un pion

        :param x: coordonnée de la ligne
        :param y: coordonnées de la colonne
        :return:
        """
        self.position=(x,y)
        return

    def atomic_moves(self,board):
        """
        Fonction permettant de créer une liste des déplacements possibles pour un pion

        :param board: plateau de jeu
        :return: une liste de déplacements possible
        """
        list = []

        if self.color=='B':
            x=self.position[0]+1
            y=self.position[1]-1
            y2=self.position[1]+1
        else :
            x=self.position[0]-1
            y=self.position[1]-1
            y2=self.position[1]+1

        if x>=0 and y>=0 and x<len(board) and y<len(board):
            if board[x][y] == '_':
                list+=self.position[0],self.position[1],x,y

        if x>=0 and y2>=0 and x<len(board) and y2<len(board):
            if board[x][y2] == '_' :
                list+=self.position[0],self.position[1],x,y2
        return list

    def atomic_capture(self,board):
        """
        Fonction permettant de créer une liste des captures possibles pour un pion

        :param board: plateau de jeu
        :return: une liste de captures possible
        """

        list = []
        color_e=''
        color_e_2=''
        if self.color=='B':
            color_e='N'
            color_e_2='Q'
        else :
            color_e='B'
            color_e_2='K'

        x=self.position[0]
        y=self.position[1]
        x_1=x-1
        y_1=y-1
        x_2=x-1
        y_2=y+1
        x_3=x+1
        y_3=y-1
        x_4=x+1
        y_4=y+1

        x_a=x_1-1
        y_a=y_1-1
        x_b=x_2-1
        y_b=y_2+1
        x_c=x_3+1
        y_c=y_3-1
        x_d=x_4+1
        y_d=y_4+1

        if x_1>=0 and y_1>=0 and x_1<len(board) and y_1<len(board) and x_a>=0 and y_a>=0 and x_a<len(board) and y_a<len(board):
            if board[x_a][y_a] == '_':
                if not board[x_1][y_1] == '_':
                    if board[x_1][y_1].get_color() == color_e or board[x_1][y_1].get_color() == color_e_2:
                        list+=self.position[0],self.position[1],x_1,y_1,x_a,y_a

        if x_2>=0 and y_2>=0 and x_2<len(board) and y_2<len(board) and x_b>=0 and y_b>=0 and x_b<len(board) and y_b<len(board):
            if board[x_b][y_b] == '_':
                if not board[x_2][y_2] == '_':
                    if board[x_2][y_2].get_color() == color_e or board[x_2][y_2].get_color() == color_e_2:
                        list+=self.position[0],self.position[1],x_2,y_2,x_b,y_b

        if x_3>=0 and y_3>=0 and x_3<len(board) and y_3<len(board) and x_c>=0 and y_c>=0 and x_c<len(board) and y_c<len(board):
            if board[x_c][y_c] == '_':
                if not board[x_3][y_3] == '_':
                    if board[x_3][y_3].get_color() == color_e or board[x_3][y_3].get_color() == color_e_2:
                        list+=self.position[0],self.position[1],x_3,y_3,x_c,y_c

        if x_4>=0 and y_4>=0 and x_4<len(board) and y_4<len(board) and x_d>=0 and y_d>=0 and x_d<len(board) and y_d<len(board):
            if board[x_d][y_d] == '_':
                if not board[x_4][y_4] == '_':
                    if board[x_4][y_4].get_color() == color_e or board[x_4][y_4].get_color() == color_e_2:
                        list+=self.position[0],self.position[1],x_4,y_4,x_d,y_d


        return list