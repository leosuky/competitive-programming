"""
https://leetcode.com/problems/maximum-subarray

Given an integer array nums, find the
subarray
with the largest sum, and return its sum.
--------------------------------------------------------------------
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        """Initialize the maximum sum as the first element in the array"""
        max_sum = nums[0]

        """set the running sum to 0"""
        curr_sum = 0

        """loop through the array"""
        for i in nums:
            """if the previously running sum < 0"""
            if curr_sum < 0:
                """
                intialize it back to zero so at to
                always get the maximum positive sum"""
                curr_sum = 0

            """ Add the current number `i` to the running sum"""
            curr_sum += i

            """
            If the running sum is greater than the max,
            replace it.
            """
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum


"""
The algorithm above has a time complexity of 0(n)
and a space complexity of 0(1)
----------------------------------------------
ARRAY --- MEDIUM
"""