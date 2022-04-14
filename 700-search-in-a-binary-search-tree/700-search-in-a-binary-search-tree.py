class Solution:    
    def searchBST(self, root: Optional[TreeNode], k: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == k:
            return root
        return self.searchBST(root.left, k) or self.searchBST(root.right, k)