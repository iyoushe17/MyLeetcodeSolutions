# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def search(self, val, root):
#         if not root:
#             return None
#         if root.val == val:
#             return root
#         return self.search(val, root.left) or self.search(val, root.right)
    
    def searchBST(self, root: Optional[TreeNode], k: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == k:
            return root
        return self.searchBST(root.left, k) or self.searchBST(root.right, k)