"""
https://leetcode.com/problems/count-number-of-nice-subarrays/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r, res = 0, 0, 0
        while r < n:
            while r < n and k > 0:
                if nums[r] % 2 != 0:
                    k -= 1
                r += 1
            i = l
            j = r
            while l < r and nums[l] % 2 == 0:
                l += 1
            while r < n and nums[r] % 2 == 0:
                r += 1
            if k == 0:
                res += (l - i + 1) * (r - j + 1)
            l += 1
            k += 1
        return res
