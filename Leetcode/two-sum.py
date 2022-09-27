"""
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
---------------------------------------------------------------------------------------
EXAMPLE 1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary to hold values
        target_dict = {}

        # iterate through the list
        for i in range(len(nums)):
            # subtract the list item from the target
            x = target - nums[i]

            # if the subtracted value exist in the dictionary
            if x in target_dict:
                # return a list of the index of subtracted value and current index
                return [target_dict[x], i]
            else:
                # assign list item as a new key and its index as the value.
                target_dict[nums[i]] = i


"""
The algorithm above has a space complexity of 0(n)
and a time complexity of 0(n)
The #in operation on line 28 is apparently 0(1) as explained here:
https://stackoverflow.com/questions/17539367/python-dictionary-keys-in-complexity
"""
