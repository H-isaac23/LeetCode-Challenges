# Given an integer array nums of unique elements, return all possible subsets(the power set).
# The solution set must not contain duplicate subsets.Return the solution in any order.
#
# Example 1:
# Input: nums = [1, 2, 3]
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
#
# Example 2:
# Input: nums = [0]
# Output: [[], [0]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            newSet = []
            for setItem in result:
                newItem = setItem + [num]
                newSet.append(newItem)
            result += newSet
        return result
