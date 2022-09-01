# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, node: TreeNode) -> int:
        count = 0
        def recurse(root, greatest):
            nonlocal count
            if not root:
                return
            
            if root.val >= greatest:
                greatest = root.val
                count += 1
                
            recurse(root.right, greatest)
            recurse(root.left, greatest)
            return
        
        recurse(node, float('-inf'))
        return count