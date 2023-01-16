"""
https://leetcode.com/problems/product-of-array-except-self/
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
------------------------------------------------------------------------------------------
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # initialize running constant
        init_n = 1
        # initialize empty array
        answer = []

        # iterate through the input array
        for i in range(len(nums)):

            # append the value of the running constant
            answer.append(init_n)

            """
            replace the running constant with it's value multiplied by the value at
            current index.
            """
            init_n *= nums[i]

            """
            So at this point, each value at index i in the answer array is the multiplication
            of all the values in the nums array before index i. Except the first element, which
            will always be 1
            """

        # re-initialize running constant
        init_n = 1

        # iterate through the input array backwards
        for j in range(len(nums)-1, -1, -1):

            """
            replace the value at each index in the answer array with its value multiplied
            by the running constant
            """
            answer[j] *= init_n

            # replace the value of the running constant as in the first loop
            init_n *= nums[j]

            """
            So this loop is the exact same as before but in reverse, which means the last elemnt
            in the answer array will always be multiplied by 1 and the first element will be the
            multiplication of all elements except itself.
            """

        return answer



"""
The algorithm above has a time complexity of 0(n)
and a space complexity of 0(1)
----------------------------------------------
ARRAY --- MEDIUM
"""
