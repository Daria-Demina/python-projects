"""
https://leetcode.com/problems/contains-duplicate-iii/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False
        window = {}
        for i in range(len(nums)):
            if i > indexDiff:
                del window[nums[i - indexDiff - 1]]
            for num in window:
                if abs(num - nums[i]) <= valueDiff:
                    return True
            window[nums[i]] = window.get(nums[i], 0) + 1
        return False
