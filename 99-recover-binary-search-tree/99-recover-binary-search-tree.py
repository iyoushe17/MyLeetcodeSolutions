# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        
        def inorder(root):
            nonlocal prev, first, middle, last
            if not root:
                return 
            inorder(root.left)
            
            # violation, increasing order not followed
            if prev.val > root.val:
                if not first:
                    first = prev
                    middle = root
                else:
                    last = root
            prev = root
            inorder(root.right)
            return
        
        first, middle, last = None, None, None
        prev = TreeNode(float('-inf'), None)
        inorder(root)
        
        if first and last:
            last.val, first.val = first.val, last.val
        elif first and middle:
            middle.val, first.val = first.val, middle.val
        