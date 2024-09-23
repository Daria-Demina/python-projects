"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=string
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        otv = 1
        new = s[0]
        for i in range(1, len(s)):
            if s[i] in new:
                while s[i] in new or len(new)>0:
                    new = new[1:]
                new = new + s[i]
                if len(new)>otv: otv = len(new)
            else:
                new = new + s[i]
                if len(new)>otv: otv = len(new)
        return otv