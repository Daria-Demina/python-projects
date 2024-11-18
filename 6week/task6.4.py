"""
https://leetcode.com/problems/arithmetic-slices/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        count = 0
        current_length = 2
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                current_length += 1
                count += current_length - 2
            else:
                current_length = 2
        return count
