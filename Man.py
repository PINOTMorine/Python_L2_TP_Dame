from Piece import *

class Man(Piece):
    """
    Classe Man, héritant de la classe Piece
    """

    def atomic_moves(self, board):
        """
        Fonction permettant de créer une liste des déplacements possibles pour un pion Man

        :param board: plateau de jeu
        :return: une liste de déplacements possibles
        """
        list = []

        if self.color == 'B':
            x = self.position[0] + 1
            y = self.position[1] - 1
            y2 = self.position[1] + 1
        else:
            x = self.position[0] - 1
            y = self.position[1] - 1
            y2 = self.position[1] + 1

        if x >= 0 and y >= 0 and x < len(board) and y < len(board):
            if board[x][y] == '_':
                list += self.position[0], self.position[1], x, y

        if x >= 0 and y2 >= 0 and x < len(board) and y2 < len(board):
            if board[x][y2] == '_':
                list += self.position[0], self.position[1], x, y2
        return list