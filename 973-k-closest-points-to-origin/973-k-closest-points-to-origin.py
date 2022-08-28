# sorting solution
class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def transform(coordinate):
            x, y = coordinate
            return x**2 + y**2
        
        points.sort(key = transform)
        return points[:k]