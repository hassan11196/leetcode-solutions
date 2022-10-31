# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        queue = []
        queue.insert(0, (root, targetSum - root.val))

        while queue:
            node, remaining_sum = queue.pop()

            if remaining_sum == 0 and node.left is None and node.right is None:
                return True

            if not node.left is None:
                queue.append((node.left, remaining_sum - node.left.val))
            if not node.right is None:
                queue.append((node.right, remaining_sum - node.right.val))

        return False
