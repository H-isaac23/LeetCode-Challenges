"""Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000"""

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        answer = []
        nodes = []
        nodes.append(root)
        while len(nodes):
            vals = []
            for _ in range(len(nodes)):
                if nodes[0]:
                    node = nodes.pop(0)
                    vals.append(node.val)
                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)
                else:
                    nodes.pop(0)
            answer.append(vals)
        return answer

# Submission Details:
# >60%/>50%
