# Given an integer array nums and an integer k, return the number of pairs(i, j) where i < j such
# that | nums[i] - nums[j] | == k.
# The value of | x | is defined as:
# x if x >= 0.
# -x if x < 0.
#
# Example 1:
# Input: nums = [1, 2, 2, 1], k = 1
# Output: 4
#
# Example 2:
# Input: nums = [1, 3], k = 3
# Output: 0
#
# Example 3:
# Input: nums = [3, 2, 1, 5, 4], k = 2
# Output: 3
#
# Constraints:
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 1 <= k <= 99

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count
# way too slow lmao
# lmao could've just iterated through the array twice smh
