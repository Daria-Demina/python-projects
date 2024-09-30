"""
https://leetcode.com/problems/wildcard-matching/description/?envType=problem-list-v2&envId=string
"""

from fnmatch import fnmatch


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if fnmatch(s, p):
            return 1
        else:
            return 0
