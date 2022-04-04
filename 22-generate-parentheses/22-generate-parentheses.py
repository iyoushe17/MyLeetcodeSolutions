class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        @lru_cache(None)
        def recurse(total, opened, s):
            if total < opened:
                return
            
            if total == 0 and opened == 0:
                ans.append(s)
                return
            
        
            # can open
            if total > opened:
                # can open more
                temp = s + "("
                recurse(total, opened + 1, temp)
                
                # can close existing
                if opened > 0:
                    temp = s + ")"
                    recurse(total - 1, opened - 1, temp)
            
            # cannot open, only close
            if total == opened:
                temp = s + ")"
                recurse(total - 1, opened - 1, temp)
            
            return
        ans = []
        recurse(n, 0, "")
        return ans