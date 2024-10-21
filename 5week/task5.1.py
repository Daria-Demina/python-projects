"""
https://leetcode.com/problems/sudoku-solver/description/?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(board: List[List[str]], row: int, col: int, num: str) -> bool:
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(9):
                if board[row][i] == num:
                    return False
                if board[i][col] == num:
                    return False
                if board[box_row + i // 3][box_col + i % 3] == num:
                    return False
            return True

        def solve(board: List[List[str]]) -> bool:
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for num in "123456789":
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if solve(board):
                                    return True
                                board[row][col] = "."
                        return False
            return True

        solve(board)
