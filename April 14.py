"""Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater
than or equal to x. You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        main = dummy
        n = []

        while main.next:
            if main.next.val < x:
                n.append(main.next)
                main.next = main.next.next
            else:
                main = main.next

        main = dummy
        while main.next and len(n):
            if n[0].val <= main.next.val:
                node = n.pop(0)
                temp = main.next
                main.next = node
                node.next = temp
            main = main.next

        while len(n):
            print("hi")
            node = n.pop(0)
            main.next = node
            main = main.next

        return dummy.next

# Submission Details:
# >80.18%

class Solution2:
    def partition(self, head: ListNode, x: int) -> ListNode:
        f = ListNode()
        b = ListNode()
        front = f
        back = b
        curr = head

        while curr:
            if curr.val < x:
                front.next = curr
                front = front.next
            else:
                back.next = curr
                back = back.next
            curr = curr.next

        front.next = b.next
        back.next = None

        return f.next

# Submission Details:
# >99%/99.10%
