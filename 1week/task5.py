"""
https://leetcode.com/problems/count-and-say/?envType=problem-list-v2&envId=string
"""

class Solution:
    def f(self, s: str) -> str:
        new = ""
        while len(s) > 0:
            k = 0
            x = s[0]
            while len(s) > 0 and s[0] == x:
                k += 1
                s = s[1:]
            new += str(k) + x
        return new
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range (n-1):
            s = self.f(s)
        return s