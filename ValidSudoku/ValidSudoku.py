class ValidSudoku:
    def __init__(self, board):
        self.board = board

    def valid_sudoku_brute_force(self):
        return self.check_rows() and self.check_columns() and self.check_sub_boxes()

    def check_rows(self):
        for row in self.board:
            counts = [0] * 9
            for val in row:
                if val == ".":
                    continue
                counts[int(val) - 1] += 1
                if counts[int(val) - 1] > 1:
                    return False
        return True

    def check_columns(self):
        for i in range(9):
            counts = [0] * 9
            for j in range(9):
                val = self.board[j][i]
                if val == ".":
                    continue
                counts[int(val) - 1] += 1
                if counts[int(val) - 1] > 1:
                    return False
        return True

    def check_sub_boxes(self):
        for i in range(9):
            start_row = 3 * (i // 3)
            start_col = 3 * (i % 3)
            counts = [0] * 9
            for j in range(3):
                for k in range(3):
                    val = self.board[start_row + j][start_col + k]
                    if val == ".":
                        continue
                    counts[int(val) - 1] += 1
                    if counts[int(val) - 1] > 1:
                        return False
        return True

