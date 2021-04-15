class TicTacToe:
    """
    Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
    A move is guaranteed to be valid and is placed on an empty block.
    Once a winning condition is reached, no more moves are allowed.
    A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
    Implement the TicTacToe class:
    TicTacToe(int n) Initializes the object the size of the board n.
    int move(int row, int col, int player) Indicates that player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.
    Follow up:
    Could you do better than O(n2) per move() operation?
    """
    def __init__(self, n: int):
        self.board = [[0]*n for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        return self.checkWinner()
        
    def checkWinner(self):
        rowCheck = self.checkRows()
        if rowCheck > 0: return rowCheck
        colCheck = self.checkColumns()
        if colCheck > 0: return colCheck
        diagCheck = self.checkDiags()
        if diagCheck > 0: return diagCheck
        return 0
        
    def checkRows(self):
        for row in self.board:
            num = row[0]
            if num == 0: continue
            row_winner = num
            for checkNum in row:
                if num != checkNum: row_winner = 0
            if row_winner > 0: return row_winner
        return 0
    
    def checkColumns(self):
        for i in range(self.n):
            num = self.board[0][i]
            if num == 0: continue
            col_winner = num
            for row in self.board:
                if row[i] != num: col_winner = 0
            if col_winner > 0: return col_winner
        return 0
    
    def checkDiags(self):
        # left to right 
        upper_left = self.board[0][0]
        upper_left_is_winner = upper_left
        for i in range(self.n):
            if self.board[i][i] != upper_left: upper_left_is_winner = 0
        if upper_left_is_winner > 0: return upper_left
        # right to left
        upper_right = self.board[0][self.n-1]
        upper_right_is_winner = upper_right
        k = self.n-1
        for j in range(self.n):
            if self.board[j][k] != upper_right: upper_right_is_winner = 0
            k -= 1
        if upper_right_is_winner > 0: return upper_right
        return 0