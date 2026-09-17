class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(len(board))]
        col_sets = [set() for _ in range(len(board[0]))]
        box_sets = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row_sets[r]) or (board[r][c] in col_sets[c]) or (board[r][c] in box_sets[r//3][c//3]):
                    return False
                else:
                    row_sets[r].add(board[r][c])
                    col_sets[c].add(board[r][c])
                    box_sets[r//3][c//3].add(board[r][c])
        return True