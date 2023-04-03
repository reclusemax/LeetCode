# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(left=root.left, right=root.right)

    def isMirror(self, left: TreeNode, right:TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val) & self.isMirror(left.left, right.right) & self.isMirror(left.right, right.left)

node03 = TreeNode(3)
node02 = TreeNode(2)
node01 = TreeNode(1, left=node03, right=node02)

node13 = TreeNode(3)
node12 = TreeNode(2)
node11 = TreeNode(1, left=node12, right=node13)
node_root = TreeNode(0, node01, node11)


#print(node_root.left.val)

sol = Solution()

print(sol.isSymmetric(node_root))