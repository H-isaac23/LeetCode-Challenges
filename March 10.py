"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:

Input: num = 3
Output: "III"
Example 2:

Input: num = 4
Output: "IV"
Example 3:

Input: num = 9
Output: "IX"
Example 4:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= num <= 3999"""


class Solution:
    def intToRoman(self, num: int) -> str:
        converted = ""

        while num:
            if num >= 1000:
                converted += "M"
                num -= 1000
            elif num >= 500:
                if num // 900 == 1:
                    converted += "CM"
                    num -= 900
                else:
                    converted += "D"
                    num -= 500
            elif num >= 100:
                if num // 400 == 1:
                    converted += "CD"
                    num -= 400
                else:
                    converted += "C"
                    num -= 100
            elif num >= 50:
                if num // 90 == 1:
                    converted += "XC"
                    num -= 90
                else:
                    converted += "L"
                    num -= 50
            elif num >= 10:
                if num // 40 == 1:
                    converted += "XL"
                    num -= 40
                else:
                    converted += "X"
                    num -= 10
            elif num >= 5:
                if num / 9 == 1:
                    converted += "IX"
                    num -= 9
                else:
                    converted += "V"
                    num -= 5
            elif num >= 1:
                if num / 4 == 1:
                    converted += "IV"
                    num -= 4
                else:
                    converted += "I"
                    num -= 1

        return converted

# Submission Detail
# Runtime: 44ms, faster than 87.75% python 3 submissions