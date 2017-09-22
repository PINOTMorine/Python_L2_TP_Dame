class Piece:
    def __init__(self, position, color):
        self.position=position
        self.color=color

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def set_position(self,x,y):
        self.position=(x,y)
        return

    def atomic_moves(self,board):
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
        list = []
        color_e=''
        if self.color=='B':
            x=self.position[0]+1
            y=self.position[1]-1
            y2=self.position[1]+1
            x_capture=x+1
            y_capture=y-1
            y2_capture=y2+1
            color_e='N'
        else :
            x=self.position[0]-1
            y=self.position[1]-1
            y2=self.position[1]+1
            x_capture=x-1
            y_capture=y-1
            y2_capture=y2+1
            color_e='B'

        if x>=0 and y>=0 and x<len(board) and y<len(board):
            if board[x][y] == color_e:
                if board[x_capture][y_capture] == '_':
                    list+=self.position[0],self.position[1],x_capture,y_capture


        if x>=0 and y2>=0 and x<len(board) and y2<len(board):
            if board[x][y2] == color_e:
                if board[x_capture][y2_capture] == '_':
                    list+=self.position[0],self.position[1],x_capture,y_capture


        return list