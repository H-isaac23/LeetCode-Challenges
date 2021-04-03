"""Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'."""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0

        stack = [-1]
        ans = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif len(stack) == 1:
                stack[0] = i
            else:
                stack.pop()
                ans = max(ans, i - stack[-1])
                print(i - stack[-1], i, stack[-1])

        return ans

# Submission Details:
# 40ms/14.6mb (beats 88%/71%)
