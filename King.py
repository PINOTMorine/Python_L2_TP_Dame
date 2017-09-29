from Piece import *
# K = White King
# Q = Black King
class King(Piece):
    def atomic_moves(self,board):
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
        list = []
        color_e=''
        if self.color=='K':
            color_e='Q'
        else :
            color_e='K'

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
                    if board[x_1][y_1].get_color() == color_e:
                        list+=self.position[0],self.position[1],x_1,y_1,x_a,y_a

        if x_2>=0 and y_2>=0 and x_2<len(board) and y_2<len(board) and x_b>=0 and y_b>=0 and x_b<len(board) and y_b<len(board):
            if board[x_b][y_b] == '_':
                if not board[x_2][y_2] == '_':
                    if board[x_2][y_2].get_color() == color_e:
                        list+=self.position[0],self.position[1],x_2,y_2,x_b,y_b

        if x_3>=0 and y_3>=0 and x_3<len(board) and y_3<len(board) and x_c>=0 and y_c>=0 and x_c<len(board) and y_c<len(board):
            if board[x_c][y_c] == '_':
                if not board[x_3][y_3] == '_':
                    if board[x_3][y_3].get_color() == color_e:
                        list+=self.position[0],self.position[1],x_3,y_3,x_c,y_c

        if x_4>=0 and y_4>=0 and x_4<len(board) and y_4<len(board) and x_d>=0 and y_d>=0 and x_d<len(board) and y_d<len(board):
            if board[x_d][y_d] == '_':
                if not board[x_4][y_4] == '_':
                    if board[x_4][y_4].get_color() == color_e:
                        list+=self.position[0],self.position[1],x_4,y_4,x_d,y_d


        return list
