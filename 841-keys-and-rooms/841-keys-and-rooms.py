# DFS SOLUTION

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for i in range(len(rooms))]
        
        def go(room):
            if visited[room]:
                return
            visited[room] = True
            keys = rooms[room]
            for key in keys:
                go(key)
            return
        
        go(0)
        for val in visited:
            if not val:
                return False
        return True