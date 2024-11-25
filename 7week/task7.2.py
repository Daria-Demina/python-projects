"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        p_count = [0] * 26
        window = [0] * 26
        otv = []
        for char in p:
            p_count[ord(char) - ord("a")] += 1
        for i in range(len(p)):
            window[ord(s[i]) - ord("a")] += 1
        dif = 0
        for i in range(26):
            if p_count[i] != window[i]:
                dif += 1
        if dif == 0:
            otv.append(0)
        for i in range(len(p), len(s)):
            new_index = ord(s[i]) - ord("a")
            old_index = ord(s[i - len(p)]) - ord("a")
            window[new_index] += 1
            if window[new_index] == p_count[new_index]:
                dif -= 1
            elif window[new_index] - 1 == p_count[new_index]:
                dif += 1
            window[old_index] -= 1
            if window[old_index] == p_count[old_index]:
                dif -= 1
            elif window[old_index] + 1 == p_count[old_index]:
                dif += 1
            if dif == 0:
                otv.append(i - len(p) + 1)
        return otv
