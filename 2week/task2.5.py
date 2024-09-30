"""
https://leetcode.com/problems/integer-to-english-words/?envType=problem-list-v2&envId=string
"""


class Solution:
    def f1(self, n: int) -> str:
        words = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }
        return words.get(n)

    def f2(self, n: int) -> str:
        otv = ""
        if n // 100 != 0:
            otv = otv + " " + self.f1(n // 100) + " Hundred"
        d = (n // 10) % 10
        if d == 0:
            otv = otv + " " + self.f1(n % 10)
        elif d == 1:
            otv = otv + " " + self.f1(n % 100)
        else:
            otv = otv + " " + self.f1(d * 10) + " " + self.f1(n % 10)
        return otv.strip()

    def numberToWords(self, num: int) -> str:
        otv = ""
        if num // 1000000 != 0:
            otv = otv + self.f2(num // 1000000) + " Million"
        if (num // 1000) % 1000 != 0:
            otv = otv + " " + self.f2((num // 1000) % 1000) + " Thousand"
        otv = otv + " " + self.f2(num % 1000)
        otv = otv.lstrip()
        return otv.strip()
