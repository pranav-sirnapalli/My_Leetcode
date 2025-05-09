# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def level_with_max_sum(root):
            if not root:
                return -1

            queue = deque([root])
            max_sum = -inf
            max_level = 0
            current_level = 0

            while queue:
                level_sum = 0
                level_size = len(queue)

                for _ in range(level_size):
                    node = queue.popleft()
                    level_sum += node.val

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                if level_sum > max_sum:
                    max_sum = level_sum
                    max_level = current_level

                current_level += 1

            return max_level
        
        res = level_with_max_sum(root)
        return res + 1