"""
https://leetcode.com/problems/contains-duplicate/
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
----------------------------------------------------------------------
Example 1:

Input: nums = [1,2,3,1]
Output: true

"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # initialize hash map to store key value pairs
        my_dict = {}

        # iterate through list items
        for i in range(len(nums)):
            # if list item already exist in dictionary keys
            if nums[i] in my_dict:
                # return True
                return True
            else:
                # assign list item as a new key and its index as the value.
                my_dict[nums[i]] = i

        # return false - all items in the list are unique.
        return False


"""
The algorithm above has a time complexity of 0(n)
and a space complexity of 0(n)
----------------------------------------------
ARRAY --- EASY
"""