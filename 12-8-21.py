"""
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree
node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The
rule is similar if there the node does not have a right child.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt_sum = 0
        self.helper(root)
        return self.tilt_sum

    def helper(self, node):
        if not node:
            return 0

        n1 = self.helper(node.left)
        n2 = self.helper(node.right)
        self.tilt_sum += abs(n1 - n2)
        return node.val + n1 + n2
