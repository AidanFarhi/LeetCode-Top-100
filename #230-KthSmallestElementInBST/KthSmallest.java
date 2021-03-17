public class KthSmallest {
    /**
     * Given the root of a binary search tree, and an integer k, 
     * return the kth (1-indexed) smallest element in the tree.
     */
    public int kthSmallest(TreeNode root, int k) {
        ArrayList<Integer> items = new ArrayList<>();
        traverseInOrder(root, items);
        return items.get(k - 1);
    }
    
    private void traverseInOrder(TreeNode node, ArrayList items) {
        if (node.left != null) {
            traverseInOrder(node.left, items);
        }
        items.add(node.val);
        if (node.right != null) {
            traverseInOrder(node.right, items);
        }
    }
}