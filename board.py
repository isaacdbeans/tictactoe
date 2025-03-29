class Board:
    def __init__(self):
        self.board_array = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ]

    def place_x(self, row, col):
        if self.board_array[row][col] == 0: 
            self.board_array[row][col] = "x"
            return True
        return False
        
    def place_o(self, row, col):
        if self.board_array[row][col] == 0: 
            self.board_array[row][col] = "o"
            return True
        return False

    def reset_board(self):
        self.board_array = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ]

    def check_for_win(self):
        for i in range(len(self.board_array)):
            if self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2] != 0:
                print("horz")
                return self.board_array[i][0]
            if self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i] != 0:
                print("vert")
                return self.board_array[0][i]
        return self.check_diagonals()
    
    def check_diagonals(self):
        if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2] != 0:
            return self.board_array[0][0]
        if self.board_array[2][0] == self.board_array[1][1] == self.board_array[2][0] != 0:
            return self.board_array[2][0]