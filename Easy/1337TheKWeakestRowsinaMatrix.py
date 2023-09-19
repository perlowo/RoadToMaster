from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return list(dict(sorted(dict(enumerate(mat)).items(), key=lambda item: item[1])).keys())[:k]

print(Solution().kWeakestRows([[1,1,0,0,0],
                        [1,1,1,1,0],
                        [1,0,0,0,0],
                        [1,1,0,0,0],
                        [1,1,1,1,1]], 
                        k = 3))