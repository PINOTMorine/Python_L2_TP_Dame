from Board import *

def update_list(list):

    list2=[]
    for i in range(0, len(list), 2):
        if (not list[i] == '') or (not list[i + 1] == ''):
            list2+=list[i],list[i + 1]

    return list2

def write_list(list):
    j=0
    for i in range(0,len(list),4):
        j+=1
        print('n°',j,'- Pion(',list[i],',',list[i+1],') vers la case (',list[i+2],',',list[i+3],')')
    return

def deplacer_piece(num,board,list):

    board.deplacement_piece(x_start,y_start,x_end,y_end)
    return

p=Board(10)

player=True
end=0
p.to_lines()


while end!=5 :
    if player==True :
        print('Joueur 1 - Pions Blancs :')
    else :
        print('Joueur 2 - Pions Noirs :')
        end += 1

    print('\nListe des cases accessibles :')
    list=p.possible_move(player)
    list=update_list(list)
    write_list(list)

    print('\nListe des captures possibles :')

    num=0
    while num>len(list)/4 or num<=0:
        num=int(input('\nAprès lecture de la liste, saisissez le numéro du déplacement souhaité'))

    p.deplacement_piece(num,list)



    player = not player
    p.to_lines()
