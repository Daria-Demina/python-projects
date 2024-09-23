"""
https://leetcode.com/problems/longest-valid-parentheses/?envType=problem-list-v2&envId=string
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        otv = 0
        if len(s)>0:
            arr = []
            arr.append(s[0])
            for i in range (1, len(s)):
                if arr[-1] == "(" and s[i] == ")": 
                    otv = otv + 2
                    del arr[-1]
                else:
                    arr.append(s[i])
        return otv

