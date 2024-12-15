"""
https://leetcode.com/problems/subarrays-with-k-different-integers/?envType=problem-list-v2&envId=sliding-window
"""

from collections import defaultdict


class Solution:
    def fun(self, nums: List[int], k: int) -> int:
        otv = 0
        l = 0
        fr = defaultdict(int)
        for r in range(len(nums)):
            if fr[nums[r]] == 0:
                k -= 1
            fr[nums[r]] += 1
            while k < 0:
                fr[nums[l]] -= 1
                if fr[nums[l]] == 0:
                    k += 1
                l += 1
            otv += r - l + 1
        return otv

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.fun(nums, k) - self.fun(nums, k - 1)
