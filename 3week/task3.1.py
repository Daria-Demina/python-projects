"""
https://leetcode.com/problems/3sum/?envType=problem-list-v2&envId=array
"""

from itertools import permutations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        otv = []
        unique_sums = set()
        for x in set(permutations(nums, r=3)):
            if sum(x) == 0:
                sorted_x = tuple(sorted(x))
                if sorted_x not in unique_sums:
                    unique_sums.add(sorted_x)
                    otv.append(list(sorted_x))
        return otv
