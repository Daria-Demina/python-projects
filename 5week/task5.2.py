"""
https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=hash-table
"""

from itertools import permutations


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        otv = []
        while len(strs) > 0:
            y = strs[0]
            arr = []
            for x in set(permutations(y)):
                s = "".join(x)
                if s in strs:
                    arr.append(s)
                    strs.remove(s)
            otv.append(arr)
        return otv
