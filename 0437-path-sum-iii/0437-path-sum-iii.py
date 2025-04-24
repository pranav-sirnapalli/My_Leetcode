# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def pathSum_a(root, targetSum):
            if root == None:
                return 0
            netSum = 0
            if root.val == targetSum:
                netSum += 1
            netSum += pathSum_a(root.left, targetSum - root.val)
            netSum += pathSum_a(root.right, targetSum - root.val)
            return netSum
            
        if root == None:
            return 0
        return self.pathSum(root.left, targetSum) + pathSum_a(root, targetSum) + self.pathSum(root.right, targetSum)
        