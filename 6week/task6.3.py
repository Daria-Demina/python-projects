"""
https://leetcode.com/problems/minimum-size-subarray-sum/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        s = 0
        mn = len(nums) + 1
        while r < len(nums):
            s += nums[r]
            r += 1
            while s >= target:
                mn = min(mn, r - l)
                s -= nums[l]
                l += 1
        return mn if mn != len(nums) + 1 else 0
