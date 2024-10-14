"""
https://leetcode.com/problems/triangle/?envType=problem-list-v2&envId=array
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        s = triangle[0][0]
        j = 0
        for i in range(1, len(triangle)):
            if j + 1 == len(triangle[i]):
                s += triangle[i][j]
            else:
                if triangle[i][j] < triangle[i][j + 1]:
                    s += triangle[i][j]
                else:
                    s += triangle[i][j + 1]
                    j += 1
        return s
