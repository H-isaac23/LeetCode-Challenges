"""Write a program to find the node at which the intersection of two singly linked lists begins."""
"""Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp = headA
        temp_two = headB
        lA = 0
        lB = 0

        while temp:
            lA += 1
            temp = temp.next

        while temp_two:
            lB += 1
            temp_two = temp_two.next

        count = 0

        if lA > lB:
            count = lA - lB
            temp = headA
            temp_two = headB
        elif lB >= lA:
            count = lB - lA
            temp = headB
            temp_two = headA

        for i in range(count):
            temp = temp.next

        while temp is not None and temp != temp_two:
            temp = temp.next
            temp_two = temp_two.next

        return temp
