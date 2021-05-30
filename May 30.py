"""Given an integer array nums, return the maximum difference between two successive elements in its sorted form.
If the array contains less than two elements, return 0.
You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 109"""


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        self.qs(nums, 0, len(nums) - 1)
        print(nums)
        left = 0
        right = 1
        ans = 0
        while right < len(nums):
            ans = max(ans, abs(nums[left] - nums[right]))
            right += 1
            left += 1

        return ans

    def qs(self, arr, l, r):
        if l >= r:
            return

        p = self.partition(arr, l, r)
        self.qs(arr, l, p - 1)
        self.qs(arr, p + 1, r)

    def partition(self, arr, l, r):
        i = l - 1
        pivot = arr[r]

        for j in range(l, r):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1
