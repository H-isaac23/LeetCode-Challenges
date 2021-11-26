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

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i

        return len(nums)
