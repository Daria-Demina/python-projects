"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        char_count = {}
        for i in s:
            char_count[i] = char_count.get(i, 0) + 1
        for i in char_count:
            if char_count[i] < k:
                return max(self.longestSubstring(substr, k) for substr in s.split(i))
        return len(s)
