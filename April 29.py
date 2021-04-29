"""Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target
value.
If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        vals = []
        for i in range(len(nums)):
            if nums[i] == target and vals == []:
                vals.append(i)
            elif i == len(nums) - 1 and len(vals) == 1 and nums[i] == target:
                vals.append(i)
            elif nums[i] == target and nums[i + 1] != target:
                vals.append(i)

            if i == len(nums) - 1 and vals == []:
                return [-1, -1]
            elif i == len(nums) - 1 and len(vals) == 1:
                vals.append(vals[0])

        return vals

# Submission Details
# >5.79%
