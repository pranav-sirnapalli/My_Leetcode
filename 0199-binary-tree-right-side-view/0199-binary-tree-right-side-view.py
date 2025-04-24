# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLength = len(q)

            for i in range(qLength):
                val = q.popleft()
                if val:
                    rightSide = val
                    q.append(val.left)
                    q.append(val.right)
            
            if rightSide:
                res.append(rightSide.val)
            
        return res



