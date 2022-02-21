# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element a
# lways exists in the array.
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -231 <= nums[i] <= 231 - 1
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        curr_majority = 0
        curr_num = None
        for num in nums:
            hashmap.setdefault(num, 0)
            hashmap[num] += 1

        for key, val in hashmap.items():
            if val > curr_majority:
                curr_num = key
                curr_majority = val
        return curr_num


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        curr_num = None

        for num in nums:
            if count == 0:
                curr_num = num
            count += (1 if num == curr_num else -1)

        return curr_num

