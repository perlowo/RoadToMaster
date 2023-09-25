class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        k = 0
        c = 0
        s = sorted(s)
        t = sorted(t)        
        while (k < len(s)) and (c < len(t)):
            if s[k] != t[c]:
                return t[c]
            k+=1
            c+=1
        return t[c]
print(Solution().findTheDifference('abcd','abcde'))