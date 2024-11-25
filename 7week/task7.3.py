"""
https://leetcode.com/problems/sliding-window-median/?envType=problem-list-v2&envId=sliding-window
"""

from sortedcontainers import SortedList


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = []
        window = SortedList()
        for i in range(len(nums)):
            window.add(nums[i])
            if i >= k:
                window.remove(nums[i - k])
            if i >= k - 1:
                if k % 2 == 0:
                    median = (window[k // 2 - 1] + window[k // 2]) / 2
                else:
                    median = window[k // 2]
                medians.append(median)
        return medians
