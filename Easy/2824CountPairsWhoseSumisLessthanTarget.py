class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        output = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (len(nums) > j > i >= 0) and (nums[i] + nums[j] < target):
                    output += 1
        return output
