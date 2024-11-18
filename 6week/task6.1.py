"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        otv = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        mx = 0
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    otv[i][j] = otv[i - 1][j - 1] + 1
                    mx = max(mx, otv[i][j])
                else:
                    otv[i][j] = 0
        return mx
