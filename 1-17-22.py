# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non - empty
# word in s.
#
# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#
# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#
# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#
# Constraints:
#
# 1 <= pattern.length <= 300
# pattern contains only lower - case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match = {}
        words = list(s.split())

        if len(pattern) != len(words):
            return False
        for i, letter in enumerate(pattern):
            if letter not in match.keys() and words[i] not in match.values():
                match[letter] = words[i]
            elif words[i] in match.values() and letter not in match.keys() or words[i] != match[letter]:
                return False

        return True
