class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        output = 0
        for i in range(len(stones)):
            for j in range(len(jewels)):
                if stones[i] == jewels[j]:
                    output += 1
        return output



print(Solution().numJewelsInStones("aA","aAAbbbb"))