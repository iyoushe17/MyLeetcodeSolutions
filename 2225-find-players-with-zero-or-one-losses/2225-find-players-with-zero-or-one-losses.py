class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        neverLost = set()
        lostOne = set()
        multipleLosses = set()
        
        for winner, loser in matches:
            if winner not in multipleLosses:
                if winner not in lostOne:
                    neverLost.add(winner)
                
            if loser not in multipleLosses:
                if loser in lostOne:
                    lostOne.remove(loser)
                    multipleLosses.add(loser)
                else:
                    lostOne.add(loser)
                if loser in neverLost:
                    neverLost.remove(loser)
        
        a = list(neverLost)
        a.sort()
        b = list(lostOne)
        b.sort()
        return [a, b]