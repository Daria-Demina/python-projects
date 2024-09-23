"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/?envType=problem-list-v2&envId=string
"""
from itertools import permutations
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        otv = []
        for x in set(permutations(words)):
            y = "".join(x)
            i = s.find(y)
            if i > -1: otv.append(i)
        return otv

