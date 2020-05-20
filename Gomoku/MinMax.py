from sys import maxsize as infinity

class MinMax:
    def __init__(self, board, turn):
        self._board = board
        self._turn = turn
        
    @staticmethod
    def move_score(consecutive, open_ends, current_turn):
        if open_ends == 0 and consecutive < 5:
            return 0
        
        if consecutive == 4:
            if open_ends == 1:
                if current_turn:
                    return 10000000000
                return 50
            elif open_ends == 2:
                if current_turn:
                    return 10000000000
                return 500000
        elif consecutive == 3:
            if open_ends == 1:
                if current_turn:
                    return 7
                return 5
            elif open_ends == 2:
                if current_turn:
                    return 10000
                return 50
        elif consecutive == 2:
            if open_ends == 1:
                return 2
            elif open_ends == 2:
                return 5
        elif consecutive == 1:
            if open_ends == 1:
                return 0.5
            elif open_ends == 2:
                return 1
        else:
            return infinity
    '''
    def check_horiz(self, x):
        consec = 0
        open_ends = 0
        score = 0
        for i in range(self._board.len):
            if self.board.data[i][x] == self._turn:
                consec += 1
            elif self._board.data[i][x] == 0 and consec > 0:
                open_ends += 1
                score += self.move_score(consec, open_ends, current_turn)
            elif self._board.data[i][x] == 0:
                open_ends = 1
            elif consec > 0:
                score += self.move_score(consec, open_ends, current_turn)
                consec = 0
                open_ends = 0
        return score
    
    def check_vertc(self, x):
        consec = 0
        open_ends = 0
        score = 0
        for i in range(self._board.len):
            if self.board.data[x][i] == self._turn:
                consec += 1
            elif self._board.data[x][i] == 0 and consec > 0:
                open_ends += 1
                score += self.move_score(consec, open_ends, current_turn)
            elif self._board.data[x][i] == 0:
                open_ends = 1
            elif consec > 0:
                score += self.move_score(consec, open_ends, current_turn)
                consec = 0
                open_ends = 0
        return score
    
    def check_diag
    
    
        
    def analise(self):
        l = []
        l.append(self.evaluate_horizontal(self._turn))
        l.append(self.evaluate_vertical(self._turn))
        l.append(self.evaluate_1st_diag(self._turn))
        l.append(self.evaluate_2nd_diag(self._turn))
        return max(l)
        
        
    def evaluate_horizontal(self, current_turn):
        #seek lose ends on the horizontal
        consec = 0
        open_ends = 0
        score = 0
        for i in range(self._board.len()):
            for j in range(self._board.len()):
                if self._board.data[i][j] == current_turn:
                    consec += 1
                elif self._board.data[i][j] == 0 and consec > 0:
                    open_ends += 1
                    score += self.move_score(consec, open_ends, current_turn)
                elif self._board.data[i][j] == 0:
                    open_ends = 1
                elif consec > 0:
                    score += self.move_score(consec, open_ends, current_turn)
                    consec = 0
                    open_ends = 0
                else:
                    open_ends = 0
            if consec > 0:
                score += self.move_score(consec, open_ends, current_turn)
            consec = 0
            open_ends = 0
        return score
            
    def evaluate_vertical(self, current_turn):
        #seek lose ends on the vertical
        consec = 0
        open_ends = 0
        score = 0
        for j in range(self._board.len()):
            for i in range(self._board.len()):
                if self._board.data[i][j] == current_turn:
                    consec += 1
                elif self._board.data[i][j] == 0 and consec > 0:
                    open_ends += 1
                    score += self.move_score(consec, open_ends, current_turn)
                elif self._board.data[i][j] == 0:
                    open_ends = 1
                elif consec > 0:
                    score += self.move_score(consec, open_ends, current_turn)
                    consec = 0
                    open_ends = 0
                else:
                    open_ends = 0
            if consec > 0:
                score += self.move_score(consec, open_ends, current_turn)
            consec = 0
            open_ends = 0
        return score
    
    def evaluate_2nd_diag(self, current_turn):
        #seek lose ends on the 2nd diagonal
        consec = 0
        open_ends = 0
        score = 0
        for sum in range(self._board.len() * 2 - 1):
            for i in range(self._board.len()):
                for j in range(self._board.len()):
                    if i + j - sum == 0:
                        if self._board.data[i][j] == current_turn:
                            consec += 1
                        elif self._board.data[i][j] == 0 and consec > 0:
                            open_ends += 1
                            score += self.move_score(consec, open_ends, current_turn)
                        elif self._board.data[i][j] == 0:
                            open_ends = 1
                        elif consec > 0:
                            score += self.move_score(consec, open_ends, current_turn)
                            consec = 0
                            open_ends = 0
                        else:
                            open_ends = 0
                if consec > 0:
                    score += self.move_score(consec, open_ends, current_turn)
                consec = 0
                open_ends = 0
        return score
    
    def evaluate_1st_diag(self, current_turn):
        #seek lose ends on the 1st diagonal
        consec = 0
        open_ends = 0
        score = 0
        for sum in range(self._board.len() * 2 - 1):
            for j in range(self._board.len()):
                for i in range(self._board.len()):
                    if i + j - sum == 0:
                        if self._board.data[i][j] == current_turn:
                            consec += 1
                        elif self._board.data[i][j] == 0 and consec > 0:
                            open_ends += 1
                            score += self.move_score(consec, open_ends, current_turn)
                        elif self._board.data[i][j] == 0:
                            open_ends = 1
                        elif consec > 0:
                            score += self.move_score(consec, open_ends, current_turn)
                            consec = 0
                            open_ends = 0
                        else:
                            open_ends = 0
                if consec > 0:
                    score += self.move_score(consec, open_ends, current_turn)
                consec = 0
                open_ends = 0
        return score
            