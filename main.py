from Board import *

def update_list(list):
    """
    Fonction qui supprime les duplicatas d'un liste

    :param list: liste à vérifier
    :return: la liste sans duplicatats
    """

    list2=[]
    for i in range(0, len(list), 2):
        if (not list[i] == '') or (not list[i + 1] == ''):
            list2+=list[i],list[i + 1]

    return list2

def write_list(list):
    """
    Fonction permettant l'affichage de la liste des déplacements possibles par un joueur

    :param list: la liste des déplacements, comprenant les coordonnées de départs et d'arrivées
    :return:
    """
    j=0
    for i in range(0,len(list),4):
        j+=1
        print('n°',j,'- Pion(',list[i],',',list[i+1],') vers la case (',list[i+2],',',list[i+3],')')
    return

def write_list_2(num,list):
    """
    Fonction permettant l'affichage de la liste des captures possibles par un joueur

    :param num: nombre de coups possibles déjà écrit (afin d'avoir une continuité)
    :param list: la liste des coups possibles, comprenant les coordonnées de départs,  et d'arrivées
    :return:
    """
    j=num
    for i in range(0,len(list),6):
        j+=1
        print('n°',j,'- Pion(',list[i],',',list[i+1],') vers la case (',list[i+4],',',list[i+5],')')
    return

def main():
    """
    Fonction main
    Fonction permettant le déroulement du jeu de dames

    :return:
    """
    p=Board(10)
    joueur1 = p.count_piece('B')
    joueur2 = p.count_piece('N')

    player=True
    list=p.possible_move(player)
    list2=p.possible_move(player)

    print('DEBUT DE LA PARTIE !!!')

    p.to_lines()


    while joueur1>0 and joueur2>0 and (len(list)>0 or len(list2)>0) :
        if player==True :
            print('Joueur 1 - ',joueur1,' Pions Blancs :')
        else :
            print('Joueur 2 - ',joueur2,' Pions Noirs :')

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
        if not color=='':
            print('Vous avez capturé un pion adverse')
            if player == True:
                joueur2-=1
            else:
                joueur1-=1



        player = not player
        p.to_lines()

    print('FIN DE LA PARTIE !!!')
    print('Joueur 1 - ',joueur1,' Pions Blancs restan(s)')
    print('Joueur 2 - ',joueur2,' Pions Noirs restan(s)')
    return

# Execution de la partie
main()