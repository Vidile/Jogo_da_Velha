import random
def começar():
    if random.randint(0,1) == 0:
        return 'player 2'
    else:
        return 'player 1'

def play_again ():
    return input ('Jogar de novo? "S" ou "N"').lower().startswith('s')

def jogada():

    l = ' '
    while not (l == 'X' or l == 'O'):
        l = input (' Jogador 1 insira X ou O: ').upper()
    if l == 'X':
        return('X','O')
    else:
        return ('O','X')

def escolha (board):
    position = ' '
    while position not in "1 2 3 4 5 6 7 8 9".split () or not checador (board,int (position)):
        position = input ('Faça sua jogada (1-9)')
        return int (position)


def checador_total(board):
    for i in range (0,10):
        if checador (board, i):
            return False
    return True

def checador (board, position):
    return board[position] == ' '

def vencedor (board,l):
    return((board[9] == l and board [8] == l and board [7] == l) or
(board[1] == l and board [2] == l and board [3] == l) or
(board[4] == l and board [5] == l and board [6] == l) or
(board[7] == l and board [5] == l and board [3] == l) or
(board[1] == l and board [5] == l and board [9] == l) or
(board[9] == l and board [6] == l and board [3] == l) or
(board[8] == l and board [5] == l and board [2] == l) or
(board[7] == l and board [4] == l and board [1] == l))




def jogo (board,l, posição):
    board[posição] = l
def display_board(board):


    print ('   !   !   ')
    print (' ' +board [7] +' ! '+board [8]+ ' ! ' +board[9])
    print ('   !   !   ')
    print ('-----------')
    print ('   !   !   ')
    print (' ' +board [4] +' ! '+board [5]+ ' ! ' +board[6])
    print ('   !   !   ')
    print ('-----------')
    print ('   !   !   ')
    print (' ' +board [1] +' ! '+board [2]+ ' ! ' +board[3])
    print ('   !   !   ')





def vencedor (board,l):
    return((board[9] == l and board [8] == l and board [7] == l) or
(board[1] == l and board [2] == l and board [3] == l) or
(board[4] == l and board [5] == l and board [6] == l) or
(board[7] == l and board [5] == l and board [3] == l) or
(board[1] == l and board [5] == l and board [9] == l) or
(board[9] == l and board [6] == l and board [3] == l) or
(board[8] == l and board [5] == l and board [2] == l) or
(board[7] == l and board [4] == l and board [1] == l))













while True:
    board = [' ']*10
    player1_marker, player2_marker = jogada()
    turn = começar()
    print (turn+ 'começa!')

    game_on = True

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = escolha(board)
            jogo (board, player1_marker,position)

        if vencedor (board, player1_marker):
            display_board(board)
            print ('Ganhou aeeeee')
            game_on = False
        else:
            if checador_total(board):
                display_board(board)
                print ('Empatou!!!!')
                break
            else:
                turn = 'Player 2'
                
        if turn == 'Player 2':
            display_board(board)
            
            position = escolha (board)
            jogo (board, player2_marker,position)

        if vencedor (board, player2_marker):
            display_board(board)
            print ('Ganhou aeeeee')
            game_on = False
        else:
            if checador_total(board):
                display_board(board)
                print ('Empatou!!!!')
                break
            else:
                turn = 'Player 1'

                
    if not play_again():
        break
