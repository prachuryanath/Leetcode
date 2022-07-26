# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      def pre(arr,root):
        if( root is None):
          return 
        arr.append(root.val)
        pre(arr,root.left)
        pre(arr,root.right)
        
      arr=[]
      pre(arr,root)
      return arr