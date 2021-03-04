import java.util.ArrayList;
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class InorderTraversal {
    /*
    Given the root of a binary tree, 
    return the inorder traversal of its nodes' values.
    */
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> l = new ArrayList<>();
        if (root != null) traverse(root, l);
        return l;
    }
    
    public void traverse(TreeNode n, List<Integer> l) {
        if (n.left != null) traverse(n.left, l);
        l.add(n.val);
        if (n.right != null) traverse(n.right, l);
    }
}