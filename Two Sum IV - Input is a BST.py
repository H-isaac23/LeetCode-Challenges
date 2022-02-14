# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such
# that their sum is equal to the given target.
#
# Example 1:
# Input: root = [5, 3, 6, 2, 4, null, 7], k = 9
# Output: true
#
# Example 2:
# Input: root = [5, 3, 6, 2, 4, null, 7], k = 28
# Output: false
#
# Constraints:
#
# The number of nodes in the tree is in the range[1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.hashmap = []
        self.target = k
        self.ans = False
        self.preorder(root)
        return self.ans

    def preorder(self, node):
        if self.ans:
            return
        if not node:
            return
        self.preorder(node.left)
        self.preorder(node.right)
        if node.val in self.hashmap:
            self.ans = True
            return
        self.hashmap.append(self.target - node.val)
