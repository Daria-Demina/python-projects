"""
https://leetcode.com/problems/fruit-into-baskets/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        i = 0
        for j, z in enumerate(fruits):
            count[z] = count.get(z, 0) + 1
            if len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
        return j - i + 1
