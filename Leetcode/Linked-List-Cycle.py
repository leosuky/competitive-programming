"""
https://leetcode.com/problems/linked-list-cycle/
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
----------------------------------------------------------------------------
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # initialize an array to store the variables
        mem_addrr = []

        # iterate through the linked list
        while head:
            b = head
            # check if the head exist in the list
            if b in mem_addrr:
                # return True if so
                return True
            else:
                # else append the head to the list and move to next node
                mem_addrr.append(b)
                head = head.next

        # return False if no circular linked list
        return False

"""
The algorithm above has a time complexity of 0(n)
and a space complexity of 0(n)
----------------------------------------------
LINKED LIST --- EASY
"""

"""
My initial brute force algorithm worked but it had terrible
performance relatively. After some research online, I decided
to use the tortoise and hare algorithm
https://dev.to/alisabaj/floyd-s-tortoise-and-hare-algorithm-finding-a-cycle-in-a-linked-list-39af
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        The tortoise and hare is basically a two pointer technique, where one pointer
        moves much faster than the other, the idea is that if both pointers are moving
        in a straight path, they'll never meet but if they were moving in circles, they
        would eventually meet at some point in the circle.
        """

        # initalize tortoise and hare
        tortoise, hare = head, head

        # since hare is faster and will get to end quicker, we iterate with it.
        while hare and hare.next:
            # tortoise moves on place
            tortoise = tortoise.next
            # hare moves two places
            hare = hare.next.next

            # if they eventually meet at any point?
            if tortoise == hare:
                # return True
                return True

        # return False if no circular linked list
        return False

"""
The algorithm above has a time complexity of 0(log (n))
and a space complexity of 0(1)
----------------------------------------------
LINKED LIST --- EASY
"""