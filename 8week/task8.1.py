"""
https://leetcode.com/problems/longest-turbulent-subarray/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        otv = 2
        l, r = 0, 1
        while r < (len(arr) - 1):
            if (arr[r] > arr[r - 1] and arr[r] > arr[r + 1]) or (
                arr[r] < arr[r - 1] and arr[r] < arr[r + 1]
            ):
                otv = max(r - l + 2, otv)
            else:
                l = r
            r += 1
        return otv
