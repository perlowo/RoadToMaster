from heapq import heapify
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] += nums[i] + nums[i]
                nums[i] = nums[i]*nums[i]
            elif nums[i] == 0:
                nums[i] = 0
            else:
                nums[i] = nums[i]*nums[i]
        return nums
            
    

print(Solution().sortedSquares([-4,-1,0,3,10]))