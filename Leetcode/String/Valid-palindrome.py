"""
https://leetcode.com/problems/valid-palindrome/
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters
include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
-----------------------------------------------------------------------

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        """ Initialise a new empty string"""
        new_str = ''

        """ loop through each character in the string"""
        for character in s:
            """ If the character is alphanumeric"""
            if character.isalnum():
                "Append it to the new string"
                new_str += character

        """ Make all characters lower case """
        new_str = new_str.lower()

        """
        this returns a boolean which is decided by the comparison operator ==
        comparing the new_str with the reversed new_str
        the [::-1] syntax is the pythonic syntax for reversing a string or list
        """
        return new_str == new_str[::-1]


"""
The algorithm above has a time complexity of 0(n)
and a space complexity of 0(n)
----------------------------------------------
STRING --- EASY
"""


# 2. An Improved solution
class Solution:
    def isPalindrome(self, s: str) -> bool:

        """ replace all characters in the string to lower case"""
        s = s.lower()
        i = 0
        j = len(s)-1

        """
        We loop using the 2 pointer technique
        """
        while i <= j:

            if not s[i].isalnum():
                """
                if the character at the left isn't alphanumeric,
                move it one step forward
                """
                i += 1
            elif not s[j].isalnum():
                """
                likewise for the rightmost character
                """
                j -= 1
            elif s[i] == s[j]:
                """
                if both characters are the same however,
                move the leftmost pointer one step forward &
                one step backward for the rightmost pointer
                """
                i += 1
                j -= 1
            else:
                """
                return False if none of the above conditions are met
                """
                return False

        return True


"""
The algorithm above has a time complexity of 0(n)
but an improved space complexity of 0(1)
"""