"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]  # Pushing the nodes that have been visited
        result = [] # Final traversal

        while(stack):   # passing through every node in stack
            tmp = stack.pop()   # Pop it as it is the last value visited
            result.append(tmp.val)  # Append it to result
            for child in tmp.children:  # As each node has n children append each child
                stack.append(child) 
        return result[::-1] # Reverse it
        