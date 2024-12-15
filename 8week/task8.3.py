"""
https://leetcode.com/problems/repeated-dna-sequences/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        seq = {}
        res = set()
        for i in range(len(s) - 9):
            substr = s[i: i + 10]
            if substr in seq:
                seq[substr] += 1
                if seq[substr] == 2:
                    res.add(substr)
            else:
                seq[substr] = 1
        return list(res)
