# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
# Example 1:
# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
#
# Example 2:
# Input: nums = [-1, 1, 0, -3, 3]
# Output: [0, 0, 9, 0, 0]
#
# Constraints:
#
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# # Follow up: Can you solve the problem in O(1) extra space
# complexity? (The output array does not count as extra space for space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        answer = [0] * len(nums)

        curr_prod = 1
        for i, num in enumerate(nums):
            curr_prod *= num
            prefix[i] = curr_prod

        curr_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            curr_prod *= nums[i]
            postfix[i] = curr_prod

        for i in range(len(nums)):
            num1 = 1
            num2 = 1
            if i - 1 >= 0:
                num1 *= prefix[i - 1]
            if i + 1 < len(nums):
                num2 *= postfix[i + 1]
            answer[i] = num1 * num2

        return answer

