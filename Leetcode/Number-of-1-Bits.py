"""
https://leetcode.com/problems/number-of-1-bits

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

    Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
----------------------------------------------------------------------------------

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:

        # this retruns the 32 bit string representation of the input decimal int
        x = f'{n:032b}'

        # initialize our count to zero
        num_of_bits = 0

        # loop through each character in the string
        for i in x:
            # if the character equals 1
            if i == "1":
                # increment the count.
                num_of_bits += 1

        # return the count
        return num_of_bits


"""
The algorithm above has a time complexity of 0(1)
and a space complexity of 0(1)
You might think its O(n) 'cuz of the for loop, its NOT.
----------------------------------------------
BINARY --- EASY
"""