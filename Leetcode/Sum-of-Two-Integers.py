"""
https://leetcode.com/problems/sum-of-two-integers/

Given two integers a and b,
return the sum of the two integers without using the operators + and -.
--------------------------------------------------------------------

Example 1:
Input: a = 1, b = 2
Output: 3
"""


# SOLUTION

"""
The only way to solve this is to use bit manipulation
The bitwise operators &, ^ and << (and, xor, left shift)

Now lets explain the solution.
-------------------------------------------------------
When we add numbers in binary, 1+0 = 1, 1+1 = 0 (carries 1), 0+0 = 0
As we can see only 1+0 equals 1 with the other 2 equaling 0
This is exactly what the bitwise xor operator does.
xor returns 1 if and only if 1 of its operands is 1.
--------------------------------------------------------
So how do we handle 1+1 = 0 (but carries 1)?
The bitwise AND, (&) only returns 1 when BOTH its operands are 1
But the & and ^ dont increase bits, they only return 0 or 1 depending on their operands
-------------------------------------------------------
The left-shift, (<<) increases bits by a specified number
Example: 1 << 2 shifts the binary 01 two places to the left
Therfore, 1 << 2: 01 becomes 0100 which equals 3 in decimal.
--------------------------------------------------------

Combining all 3 bitwise operators can help us add two numbers together.
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:

        # START LOOP
        while True:
            """
            return the xor result to the 1st integer variable
            return the and result to the 2nd integer variable
            """
            a, b = (a ^ b), (a & b)

            # if the bitwise and result is greater than zero
            if b > 0:
                # shift the number by one and continue the loop
                b = b << 1
            else:
                # when the bitwise and becomes zero, we've completed the addition
                # the last bitwise xor is the result.
                return a


# WARNING!!!
"""
While this algorithm is Technically Correct, you will run into time limit exceeded
errors because of the way Python implements its int class.
(it's an infinite lenght bit integer) while that makes Python very good at handling
big numbers, it also means its super inefficient at smaller numbers.
----------------------------------------
You're better off using a statically typed language for this task.
"""

"""
The algorithm above has a time complexity of 0(1)
and a space complexity of 0(1)
----------------------------------------------
BINARY --- MEDIUM
"""