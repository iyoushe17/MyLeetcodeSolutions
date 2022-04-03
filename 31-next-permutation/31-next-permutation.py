class Solution:
    
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # iterate num from right:
        idx = len(nums) - 2
        while idx >= 0 and nums[idx] >= nums[idx + 1]:
            idx -= 1 
        if idx >= 0:
            swapIdx = len(nums) - 1
            # hunt for a number just larger than nums[idx], ]
            # the search space is a increasing right to left
            while nums[swapIdx] <= nums[idx]:
                swapIdx -= 1

            nums[idx], nums[swapIdx] = nums[swapIdx], nums[idx]
            
        l = nums[idx + 1:]
        l = l[::-1]
        nums[idx + 1:] = l
        
            
            
                