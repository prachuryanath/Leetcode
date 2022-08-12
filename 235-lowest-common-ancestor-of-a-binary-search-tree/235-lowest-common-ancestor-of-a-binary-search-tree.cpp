/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
  TreeNode* dfs(TreeNode* root,TreeNode* a,TreeNode* b){
    if(!root) return NULL;
    if(root==a||root==b) return root;
    TreeNode* l=dfs(root->left,a,b);
    TreeNode* r=dfs(root->right,a,b);
    if(l && r) return root;
    if(l) return l;
    if(r) return r;
    return NULL;
  }
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        return dfs(root,p,q);
    }
};