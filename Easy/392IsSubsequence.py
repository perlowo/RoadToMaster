class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tryresult = []
        for i in range(len(t)):
            for j in range(len(s)) :
                if s[j] == t[i]:
                    tryresult.append(s[j])
                    s.replace(s[j],'')
        if (''.join(tryresult)) == s:
            print(''.join(tryresult))
            print(s)
            return True
        else:
            return False
print(Solution().isSubsequence("axc","ahbgdc"))
print("-------------")
print(Solution().isSubsequence("abc","ahbgdc"))
print(Solution().isSubsequence("bb","ahbgdc"))
print(Solution().isSubsequence("abc","ahbgdc"))