
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class InorderTraversal:
    """
    Given the root of a binary tree, 
    return the inorder traversal of its nodes' values.
    """
    def inorderTraversal(self, root):
        l = []
        if root:
            self.traverse(root, l)
        return l
        
    def traverse(self, node, l):
        if (node.left):
            self.traverse(node.left, l)
        l.append(node.val)
        if (node.right):
            self.traverse(node.right, l)