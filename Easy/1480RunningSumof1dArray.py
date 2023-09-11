from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        sums = 0
        for i in range(len(nums)):
            output.append(nums[i] + sums)
            sums += nums[i]
        return output

