"""
https://leetcode.com/problems/next-permutation/?envType=problem-list-v2&envId=array
"""

from itertools import permutations


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        res = set()
        for x in permutations(sorted(nums)):
            res.add(x)
        otv = tuple(sorted(res))
        f = 0
        for i in otv:
            if f == 1:
                nums[:] = list(i)
                break
            if list(i) == nums and i != otv[-1]:
                f = 1
        if f == 0:
            nums[:] = list(otv[0])
