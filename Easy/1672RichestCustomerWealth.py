from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        lista = []
        for i in range(len(accounts)):
            lista.append(sum(accounts[i]))
        for i in range(len(lista)):
            if lista[i] >= richest:
                richest = lista[i]
        return richest

print(Solution().maximumWealth([[1,2,3],[4,5,6]]))