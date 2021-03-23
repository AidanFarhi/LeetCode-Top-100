# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SortedArrToBST:
    """
    Given an integer array nums where the elements are sorted in ascending order, 
    convert it to a height-balanced binary search tree.
    A height-balanced binary tree is a binary tree in which the depth of 
    the two subtrees of every node never differs by more than one.
    """
    def sortedArrayToBST(self, nums):
        
        def helper(left, right):
            
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            root = TreeNode(nums[mid])
            
            root.left = helper(left, mid-1)
            
            root.right = helper(mid+1, right)
            
            return root
        
        return helper(0, len(nums)-1)