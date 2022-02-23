# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# Constraints:
# 1 <= n <= 45
#
class Solution:
    def climbStairs(self, n: int) -> int:
        self.visited = {}
        return self.helper(n)

    def helper(self, level):
        if level in self.visited:
            return self.visited[level]

        if level == 1 or level == 2:
            return level
        elif level < 1:
            return 0
        ways = self.helper(level - 1) + self.helper(level - 2)
        self.visited[level] = ways
        return ways

