"""
https://leetcode.com/problems/median-of-two-sorted-arrays/?envType=problem-list-v2&envId=array
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        res = 1.0
        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] > nums2[0]:
                arr.append(nums2[0])
                nums2.pop(0)
            else:
                arr.append(nums1[0])
                nums1.pop(0)
        if len(nums1) > 0:
            arr.extend(nums1)
        if len(nums2) > 0:
            arr.extend(nums2)
        if len(arr) % 2 == 1:
            res = res * arr[len(arr) // 2]
        else:
            res = res * (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
        return res
