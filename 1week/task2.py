"""
https://leetcode.com/problems/zigzag-conversion/?envType=problem-list-v2&envId=string
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        x = 2*numRows - 2
        if x == 0: return s
        lst = []
        new = ""
        for i in range(numRows):
            lst.append("")
        for i in range (len(s)):
            if i%x < numRows: lst[i%x] = lst[i%x] + s[i]
            else : lst[x - i%x] = lst[x - i%x] + s[i]
        for i in range (numRows):
            new = new + lst[i]
        return new
