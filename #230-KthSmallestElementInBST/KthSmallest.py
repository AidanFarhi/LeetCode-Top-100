class KthSmallest:
    """
    Given the root of a binary search tree, and an integer k, 
    return the kth (1-indexed) smallest element in the tree.
    """
    def kthSmallest(self, root, k: int) -> int:
        items = []  # Maintain a list of node values
        self.inOrderTraversal(root, items)  # Traverse in order
        return items[k - 1]  # Items will be in sorted order so we can access kth smallest easily
    
    def inOrderTraversal(self, node, items):
        if node.left:
            self.inOrderTraversal(node.left, items)
        items.append(node.val)
        if node.right:
            self.inOrderTraversal(node.right, items)