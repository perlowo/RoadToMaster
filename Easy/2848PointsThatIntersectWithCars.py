from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        secik = set()
        for start, end in nums:
            secik.update(set(range(start,end+1)))
        return(len(secik))

print(Solution().numberOfPoints([[3,6],[1,5],[4,7]]))