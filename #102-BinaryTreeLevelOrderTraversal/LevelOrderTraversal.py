from collections import deque
"""
Definition for a binary tree node:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class LevelOrderTraversal:
    """
    Given the root of a binary tree, 
    return the level order traversal of its nodes' values. 
    (i.e., from left to right, level by level).
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
    """
    def levelOrder(self, root):
        if root is None: return []
        result = []        
        q = deque([root])  # Create a queue to add nodes
        while q:           # While the queue is not empty
            current_level_nodes = [] # This will hold all the values for the current level
            N = len(q)               # This will be the number of node vals to add on each level
            for _ in range(N):
                n = q.popleft()  # Take current node from q
                current_level_nodes.append(n.val)  # add it's value to the current_level_nodes[]
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            result.append(current_level_nodes)  # add the values of this level to the result
        return result
            
    
        
        
        
        