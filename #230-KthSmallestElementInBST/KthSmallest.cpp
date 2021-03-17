class KthSmallest {
    /* 
    * Given the root of a binary search tree, and an integer k, 
    * return the kth (1-indexed) smallest element in the tree.
    */ 
public:
    int kthSmallest(TreeNode* root, int k) 
    {
        vector<int> items;
        traverseInOrder(root, &items);
        return items.at(k - 1);
    }
    
    void traverseInOrder(TreeNode *node, vector<int> *items) 
    {
        if (node->left != NULL) 
        {
            traverseInOrder(node->left, items);
        }
        items->push_back(node->val);
        if (node->right != NULL) 
        {
            traverseInOrder(node->right, items);
        }
    }
};