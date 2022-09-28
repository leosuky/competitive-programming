"""
https://leetcode.com/problems/reverse-linked-list/
Given the head of a singly linked list, reverse the list, and return the reversed list.
---------------------------------------------------------------------
Example 1
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        The most optimal way to reverse a linked list is iteratively.
        We can't interate over a linked list like we do for list or
        dictionaries, to reverse a signly linked list, we have to redirect
        its pointers

        Explanation
        1 -> 2 -> 3 -> 4 -> 5 -> None
        None <- 1 <- 2 <- 3 <- 4 <- 5
        """

        # set initial previous value to None like the explanation above
        prev = None
        # copy the head which points to all the other nodes in the LL
        curr = head

        # iterate through until curr becomes None
        while curr:
            # assign the next node from the current node to forward
            fwrd = curr.next

            # replace the next value of current node with prev node
            # which will be None for the first iteration
            curr.next = prev

            # the previous value now becomes the current value with
            # pointer to the previous value.
            prev = curr

            # assign the next node as the current value and iterate again.
            curr = fwrd

        # At the end the previous value becomes the head and points to all
        # nodes in the linked list.
        return prev

"""
The algorithm above has a time complexity of 0(n)
and a space complexity of 0(1)
----------------------------------------------
LINKED LIST --- EASY
"""
