"""
https://leetcode.com/problems/subsets-ii/?envType=problem-list-v2&envId=array
"""

from itertools import combinations


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums) + 1):
            for combo in combinations(nums, i):
                result.add(combo)
        return list(map(list, result))
