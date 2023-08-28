#Create a tic tac toe
import os
import replit

#define player
class Player:
    def __init__(self,symbol):
        self.name= f'Player {symbol}'
        self.mark=  symbol
        self.current_move=None
        self.all_moves= []

    def add_move(self,move):
        self.all_moves.append(move)

ALL_SPACES= [1,2,3,4,5,6,7,8,9]
BLANK=" "
lines= "------"
#create board
def create_start_board():
    board= {str(space):BLANK for space in ALL_SPACES}
    return board

def create_str_board(board):


    string_board='''|{}|{}|{}  1|2|3\n------\n|{}|{}|{}  4|5|6\n------\n|{}|{}|{}  7|8|9'''.format(board['1'],board['2'],board['3'],
                                                                                    board['4'],board['5'],board['6'],
                                                                                    board['7'],board['8'],board['9'])
    return string_board




def get_update_board(current_player,game_board):
    game_board[current_player.move]= current_player.mark
    return game_board

def is_winner(board,current_player):
    b,p= board, current_player.mark
    if (b['1']==p and b['2']==p and b['3']==p):
        print(f'Player {current_player.mark}, Wins') 
        return True
    if (b['4']==p and b['5']==p and b['6']==p):
        print(f'Player {current_player.mark}, Wins') 
        return True
    if (b['7']==p and b['8']==p and b['9']==p): 
        print(f'Player {current_player.mark}, Wins')
        return True
    if (b['1']==p and b['4']==p and b['7']==p):
        print(f'Player {current_player.mark}, Wins') 
        return True
    if (b['2']==p and b['5']==p and b['8']==p): 
        print(f'Player {current_player.mark}, Wins')
        return True
    if (b['3']==p and b['6']==p and b['9']==p): 
        print(f'Player {current_player.mark}, Wins')
        return True
    if (b['1']==p and b['5']==p and b['9']==p): 
        print(f'Player {current_player.mark}, Wins')
        return True
    if (b['3']==p and b['5']==p and b['7']==p):
        print(f'Player {current_player.mark}, Wins') 
        return True
    return False

def is_board_full(board):
    if BLANK in board.values():
        return False
    print(f'Board is full Game over')
    return True






if __name__ == '__main__':
    #create players
    player_1= Player('X')
    player_2 = Player('O')
    current_player=player_1
    next_player= player_2

    #create start board
    board= create_start_board()

    #create string board
    str_gameboard= create_str_board(board)

    print("Start of tic tac game")
    print(str_gameboard)
    #test to see if there is a winner
    winner=is_winner(board,current_player)
    #test if board is full
    board_full=is_board_full(board)

    while not winner or not board_full :
        #ask player to select move by picking number between 1-9
        current_player.move= input(f'{current_player.name}, please choose your play by choosing the number of the position:\n>>')
        updated_board= get_update_board(current_player,board)
        board=updated_board
        str_gameboard= create_str_board(updated_board)
        replit.clear()
        #show board to players
        print(str_gameboard)
        #test to see if there is a winner
        winner=is_winner(board,current_player)
        #test if board is full
        board_full=is_board_full(board)
        current_player,next_player=next_player,current_player
       

       