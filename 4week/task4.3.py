"""
https://leetcode.com/problems/maximum-subarray/?envType=problem-list-v2&envId=array
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = []
        arr.append(nums[0])
        for i in range(1, len(nums)):
            mx = max(nums[i], nums[i - 1] + nums[i], arr[i - 1] + nums[i])
            arr.append(mx)
        res = max(arr)
        return res
