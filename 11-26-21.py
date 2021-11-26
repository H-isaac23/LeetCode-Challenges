# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])

        return max(dp)