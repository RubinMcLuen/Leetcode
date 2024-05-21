import collections


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
    

    def valid_sudoku_one_pass(self):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if self.board[r][c] == ".":
                    continue
                if (self.board[r][c] in rows[r] or
                    self.board[r][c] in cols[c] or
                    self.board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(self.board[r][c])
                cols[c].add(self.board[r][c])
                squares[(r // 3, c // 3)].add(self.board[r][c])
        return True


