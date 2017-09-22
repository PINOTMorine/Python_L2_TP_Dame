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

def write_list_2(num,list):
    j=num
    for i in range(0,len(list),6):
        j+=1
        print('n°',j,'- Pion(',list[i],',',list[i+1],') vers la case (',list[i+4],',',list[i+5],')')
    return

p=Board(10)


player=True
end=0

p.to_lines()


while end!=2 :
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
    list2=p.possible_capture(player)
    list2=update_list(list2)
    write_list_2(len(list)//4,list2)

    num=0
    while num>len(list)/4+len(list2)/6 or num<=0:
        num=int(input('\nAprès lecture des listes, saisissez le numéro du déplacement souhaité'))

    color=p.deplacement_piece(num,list,list2)
    print(color)


    player = not player
    p.to_lines()
