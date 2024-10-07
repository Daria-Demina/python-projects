"""
https://leetcode.com/problems/minimum-path-sum/?envType=problem-list-v2&envId=array
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row = len(grid)
        for i in range(1, col):
            grid[0][i] = grid[0][i - 1] + grid[0][i]
        for i in range(1, row):
            grid[i][0] = grid[i - 1][0] + grid[i][0]
        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]
