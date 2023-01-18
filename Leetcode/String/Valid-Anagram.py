"""
https://leetcode.com/problems/valid-anagram

Given two strings s and t,
return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.
-----------------------------------------------------------------------

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        First get the length of both strings
        """
        len_s = len(s)
        len_t = len(t)

        """ If both lenghts are unequal, we know its False"""
        if len_t != len_s:
            return False

        """The sorted function returns a sorted list of characters"""
        sort_s = sorted(s)
        sort_t = sorted(t)

        """ Loop through the lenght of the string which is the same as the list"""
        for i in range(len_t):
            """ if two characters at the same position aren't equal, we know its False"""
            if sort_s[i] != sort_t[i]:
                return False

        """ If we get to this point, then we know we have a valid anagram"""
        return True



"""
The algorithm above has a time complexity of 0(n.log(n))
because of the sorting and a space complexity of 0(n + m)
----------------------------------------------
STRING --- EASY
"""


# 2. Another Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """Same as before, return false if lenghts are unequal"""
        if len(t) != len(s):
            return False


        """
        The sorted function return an array of characters
        return True if both sorted arrays are equal
        """
        return True if (sorted(s) == sorted(t)) else False


"""
The algorithm above has a time complexity of 0(n.log(n))
because of the sorting and a space complexity of 0(n + m)
----------------------------------------------
more or less the same as the first one.
"""


# 3. Most Optimal Solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False

        """
        We define all 26 letters in the alphabet
        """
        letters = 'esiarntolcdugpmhbyfvkwzxjq'

        """ Loop through all the letters"""
        for letter in letters:
            """
            If the count of each letter isnt equal from both
            input strings, return False
            """
            if s.count(letter) != s.count(letter):
                return False

        return True


"""
The algorithm above has a time complexity of 0(n)
and a space complexity of 0(1)
----------------------------------------------
Now you probably think its O(n) because of the for-loop,
its not however, the for-loop is O(1) because it loops over 26 letters
constantly no matter the size of the input.
So why isn't the algorithm o(1)? Well, the str.count() in python performs
its count operation in linear time O(n) so our overrall time complexity
for the algorithm is O(n)
"""