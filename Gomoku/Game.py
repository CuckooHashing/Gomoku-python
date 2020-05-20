from texttable import Texttable
from copy import deepcopy
from random import choice

class GameException(Exception):
    def __init__(self, msg):
        self._msg = msg
    @property
    def message(self):
        return self._msg

class Board:
    '''
    gameboard
    '''
    def __init__(self):
        self._data = []
        for i in range(15):
            self._data.append([0] * 15)
            
        '''
        symbols - O or X
        '''
    @property
    def data(self):
        return self._data
    
    @property
    def len(self):
        return len(self._data)
    
    def move(self, x, y, symbol):
        if x not in list(range(15)) or y not in list(range(15)): 
            raise GameException("Please try to move INSIDE the board")
        if symbol not in ['X', 'O']:
            raise GameException("Do try to stick to your chosen character")
        if self._data[x][y] != 0:
            raise GameException("Do you not see that the square was already played?")
        
        d = {'X':1, 'O':-1}
        self._data[x][y] = d[symbol]
        
    def get_empty(self):
        squares = []
        
        for i in range(15):
            for j in range(15):
                if self._data[i][j] == 0:
                    squares.append((i, j))
        return squares
            
    def __str__(self):
        t = Texttable()
        '''
        build row header
        '''
        res = [' ']
        for i in range(15):
            res.append(i + 1)
        
        t.header(res)
        d = {0:" " , -1:"O" , 1:"X"}
        for i in range(15):
            pretty = deepcopy(self._data[i])
            for j in range(len(pretty)):
                pretty[j] = d[pretty[j]]
            t.add_row([i + 1] + pretty)
        return t.draw()
    
    def won(self, x, y):
        if self._data[x][y] != 0:
            #columns
            nr = 1
            for i in range(1, 5):
                if x - i < 0:
                    break
                else:
                    if self._data[x][y] == self._data[x - i][y]:
                        nr += 1
                    else:
                        break
            if nr == 5:
                return True
            for i in range(1, 5):
                if x + i > 14:
                    break
                else:
                    if self._data[x][y] == self._data[x + i][y]:
                        nr += 1
                    else:
                        break
            if nr == 5:
                return True
            #lines
            nr = 1
            for i in range(1, 5):
                if y - i < 0:
                    break
                else:
                    if self._data[x][y] == self._data[x][y - i]:
                        nr += 1
                    else:
                        break
            if nr == 5:
                return True
            for i in range(1, 5):
                if y + i > 14:
                    break
                else:
                    if self._data[x][y] == self._data[x][y + i]:
                        nr += 1
                    else:
                        break
            if nr == 5:
                return True
            #diagonal 1
            nr = 1
            for i in range(1, 5):
                if x - i < 0 and y - i < 0:
                    break
                else:
                    if self._data[x][y] == self._data[x - i][y - i]:
                        nr += 1
                    else:
                        break
            if nr == 5:
                return True
            for i in range(1, 5):
                if x + i > 14 and y + i > 14:
                    break
                else:
                    if self._data[x][y] == self._data[x + i][y + i]:
                        nr += 1
                    else:
                        break
            if nr == 5:
                return True
            #diagonal 2
            nr = 1
            for i in range(1, 5):
                if x - i < 0 and y + i > 14:
                    break
                else:
                    if self._data[x][y] == self._data[x - i][y + i]:
                        nr += 1
                    else:
                        break
            if nr == 5:
                return True
            for i in range(1, 5):
                if x + i > 14 and y - i < 0:
                    break
                else:
                    if self._data[x][y] == self._data[x + i][y - i]:
                        nr += 1
                    else:
                        break
            if nr == 5:
                return True
            
            return False
        else:
            return False
        
    def tie(self):
        return self.won == False and len(self.get_empty()) == 0
    
class Game:
    def __init__(self):
        self._board = Board()
    
    @property
    def board(self):
        return self._board
    
    def human_move(self, x, y):
        self._board.move(x, y, 'X')
    
    def stupid_AI_move(self, x, y):
        neigh = [ (x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x+1, y+1), (x, y+1) ]
        option = choice(neigh)
        while True:
            if option in self.board.get_empty():
                self._board.move(option[0], option[1], 'O')
                return option
            else:
                option = choice(neigh)
                
    
    def smart_AI_move(self):
        pass
    
class UI:
    def __init__(self, game):
        self._game = game
        
    def parse_move(self):
        while True:
            try:
                moving = input("Enter move \n >").split()
                return (int(moving[0]) - 1, int(moving[1]) - 1)
            except Exception:
                print("Do try to give a valid move")
            
    def start(self):
        b = self._game.board
        player_turn = True
        last_move = (-1, -1)
        
        while (b.won(last_move[0], last_move[1]) == False and b.tie() == False) or last_move == (-1, -1):
            if player_turn:
                print(self._game.board)
                try:
                    move = self.parse_move()
                    last_move = move
                    self._game.human_move(move[0], move[1])
                except GameException as e:
                    print(e)
                    continue
            else:
                last_move = self._game.stupid_AI_move(last_move[0], last_move[1])
                
            player_turn = not player_turn
            
        print("Game over!")
        print(b)
        if b.won(last_move[0], last_move[1]):
            if player_turn == True:
                print("Computer won!")
            else:
                print("Congratulation! You won!")
        else:
            print("Somehow you managed a tie")

print("Welcome to the Renju variant of Gomoku!") 
g = Game()
ui = UI(g)
ui.start()
