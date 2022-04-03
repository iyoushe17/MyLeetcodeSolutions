class Solution:
    def howManyCandiesGreaterOrEqual(self, candies, mid):
        total = 0
        for i in candies:
            total += i // mid
        return total
         
    def maximumCandies(self, candies: List[int], kids: int) -> int:
        start = 1
        totalCandies = sum(candies)
        end = totalCandies // kids
        if totalCandies < kids:
            return 0
        ans = 0
        while start <= end:
            mid = start + (end - start) // 2
            
            # are there "kids" number of total piles?
            if self.howManyCandiesGreaterOrEqual(candies, mid) >= kids:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
                
        
        return ans