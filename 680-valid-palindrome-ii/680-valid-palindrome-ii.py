class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        
        while start < end:
            if s[start] != s[end]:
                # skip the start element, and keep the end element
                skipStart = s[start+1 : end + 1]
                # skip the end element, and keep the start element
                skipEnd = s[start : end]
                
                return skipStart == skipStart[::-1] or skipEnd == skipEnd[::-1]
            start += 1
            end -= 1
        
        return True