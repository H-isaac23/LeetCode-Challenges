"""Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.vals = []
        self.helper(root, 1, root)
        self.vals.pop(0)
        return sum(self.vals) // 2

    def helper(self, node, d, bn):
        if node is None:
            if self.vals == []:
                self.vals.append(d)
                self.vals.append(bn.val)
            else:
                if d > self.vals[0]:
                    self.vals.clear()
                    self.vals.append(d)
                    self.vals.append(bn.val)
                elif d == self.vals[0]:
                    self.vals.append(bn.val)
            print(self.vals)
            return
        print(node.val)

        self.helper(node.right, d + 1, node)
        self.helper(node.left, d + 1, node)


class Solution2:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = []
        queue.append(root)

        while len(queue):
            val = 0
            for _ in range(len(queue)):
                x = queue.pop(0)
                if x.right:
                    queue.append(x.right)
                if x.left:
                    queue.append(x.left)
                val += x.val
            if len(queue) == 0:
                return val
