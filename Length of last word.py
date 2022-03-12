# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in
# the string.
# A word is a maximal substring consisting of non-space characters only.
#
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#
# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastCount = 0
        currCount = 0

        for x in s:
            if x == " ":
                currCount = 0
            else:
                currCount += 1
            lastCount = currCount if currCount != 0 else lastCount

        return lastCount
        # 71%/88%

class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    #87%/88%
