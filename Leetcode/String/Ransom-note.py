"""
https://leetcode.com/problems/ransom-note
Given two strings ransomNote and magazine, return true if ransomNote
can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
---------------------------------------------------------------------
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        """
        Loop through every letter in the ransomNote
        """
        for letter in ransomNote:
            """
            If the count of the letter in the ransom note is
            greater than the count in the magazine, then we
            know that word can't be formed, return False
            """
            if ransomNote.count(letter) > magazine.count(letter):
                return False

        """
        If it gets here, then we're good, return true.
        """
        return True


"""
The algorithm above has a time complexity of 0(n**2)
and a space complexity of 0(1)
- str.count() is O(n)
While our space complexity is very good,
our time complexity can be improved.
----------------------------------------------
STRINGS --- EASY
"""

# 2. Optimized Solution

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        """
        Initialize dictionary to store letters and the amount of
        times they appear
        """
        letter_dict = {}

        """
        loop through the ransomNote
        """
        for letter in ransomNote:
            """
            if the current letter already exist in the dictionary
            """
            if letter in letter_dict:
                """ increment its count"""
                letter_dict[letter] += 1
            else:
                """ else add it to the dictionary"""
                letter_dict[letter] = 1

        """ loop through all keys in the didctionary """
        for key in letter_dict:
            """
            if the key count in the magazine is less than its
            respective count in the dictionary, then we know that
            the letter appeared more times in the ransomNote than
            in the magazine, so return False.
            """
            if magazine.count(key) < letter_dict[key]:
                return False

        """
        If it gets here, then we're good, return true.
        """
        return True

"""
The algorithm above has a time complexity of 0(n.log(n))
and a space complexity of 0(n)
- str.count() is O(n)

----------------------------------------------
STRINGS --- EASY
"""