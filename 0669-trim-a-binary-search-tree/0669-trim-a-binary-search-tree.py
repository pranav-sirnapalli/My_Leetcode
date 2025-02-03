# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def helper(root, l, h):
            if root == None:
                return None
            if low > root.val:
                return helper(root.right, low, high)
            elif high < root.val:
                return helper(root.left, low, high)
            else:
                root.left = helper(root.left, low, high)
                root.right = helper(root.right, low, high)
                return root
        return helper(root, low, high)