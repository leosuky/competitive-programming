"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
----------------------------------------------------------------------------
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:

        """
        Since we now that the list is partially sorted, we can use
        Binary Search
        """

        # initialize left most and right most indexes
        left = 0
        right = len(nums) - 1

        # while both indexes arent eaqual
        while left < right:

            # get the middle index of the remaining array
            mid = (left + right) // 2

            # if the middle number is greater than the rightmost number
            if nums[mid] > nums[right]:
                # move the left index 1 place after the middle
                # essentially halving the array
                left = mid + 1

            else:
                # otherwise, move the right index to the middle
                # this also halves the array
                right = mid

        """
        At some point, there'll be one element left in the array
        at which, we break out of the loop because the left index
        will be equal to the right.
        Then we just return the elemnt in the array
        """
        return nums[left] # nums[right] is also correct



"""
The algorithm above has a time complexity of 0(log n)
and a space complexity of 0(1)
----------------------------------------------
ARRAY --- MEDIUM
"""
