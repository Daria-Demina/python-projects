"""
https://leetcode.com/problems/string-to-integer-atoi/?envType=problem-list-v2&envId=string
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        st = s.lstrip()
        f = 0
        if st[0] == "-":
            f = -1
            st = st[1:]
        elif st[0] == "+":
            f = 1
            st = st[1:]
        res = 0
        for i in range(len(st)):
            if st[i] in "0123456789":
                res = res * 10 + int(st[i])
            else:
                break
        if f != 0:
            res = res * f
        return res
