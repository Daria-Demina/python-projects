"""
https://leetcode.com/problems/longest-repeating-character-replacement/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        c_freq = {}
        otv = 0
        for r in range(len(s)):
            if not s[r] in c_freq:
                c_freq[s[r]] = 0
            c_freq[s[r]] += 1
            cells_count = r - l + 1
            if cells_count - max(c_freq.values()) <= k:
                otv = max(otv, cells_count)
            else:
                c_freq[s[l]] -= 1
                if not c_freq[s[l]]:
                    c_freq.pop(s[l])
                l += 1
        return otv
