# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append((root, 0))
        currSum = 0
        currTotal = 0
        currLevel = 0
        ans =[]
        
        while q:
            front = q[0]
            
            q.popleft()
            if front[0].left:
                q.append((front[0].left, front[1] + 1))
            if front[0].right:
                q.append((front[0].right, front[1] + 1))
            
            if front[1] > currLevel:
            # calculate average, the level is completed
                average = currSum / currTotal
                ans.append(average)
                
                currSum = front[0].val
                currTotal = 1
                currLevel += 1
            
            else:
                currSum += front[0].val
                currTotal += 1
        ans.append(currSum/currTotal)
        return ans
                