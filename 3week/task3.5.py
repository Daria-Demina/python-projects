"""
https://leetcode.com/problems/first-missing-positive/?envType=problem-list-v2&envId=array
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        otv = -1
        for i in range(1, max(nums)):
            if i not in nums:
                otv = i
                break
        if otv == -1:
            otv = max(nums) + 1
        return otv
