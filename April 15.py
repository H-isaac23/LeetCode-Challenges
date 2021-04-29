"""The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is
the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:

0 <= n <= 30"""

class Solution:
    def fib(self, n: int) -> int:
        self.vals = [0] * (31)
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        return self.helper(n - 1) + self.helper(n - 2)

    def helper(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        if self.vals[n] == 0:
            val = self.helper(n - 1) + self.helper(n - 2)
            self.vals[n] = val
            return self.vals[n]
        else:
            return self.vals[n]

from math import sqrt

class Solution:
    def fib(self, n: int) -> int:
        sqrt5 = sqrt(5)
        return int((pow(1 + sqrt5, n) - pow(1 - sqrt5, n)) / pow(2, n) / sqrt5)