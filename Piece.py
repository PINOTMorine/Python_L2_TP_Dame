class Piece:
    def __init__(self, position, color):
        self.position=position
        self.color=color

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def atomic_moves(self,board):
        list= []

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
                #print('>(',x,',',y,')')
                list+=x,y

        if x>=0 and y2>=0 and x<len(board) and y2<len(board):
            if board[x][y2] == '_' :
                #print('>(',x,',',y2,')')
                list+=x,y2

        return list