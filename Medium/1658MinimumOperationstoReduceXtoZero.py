from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        print(f"target {target}")
        
        if target < 0:
            return -1
        
        i, current_sum, min_ops = 0, 0, 10**9 + 1  
        
        for j in range(len(nums)):
            current_sum += nums[j]
            print(f"current sum for {current_sum}")
            
            while current_sum > target:
                current_sum -= nums[i]
                print(f"current sum while {current_sum}")
                i += 1
            
            if current_sum == target:
                min_ops = min(min_ops, len(nums) - (j - i + 1))
                # print(len(nums) - (j - i + 1))
                # print(min_ops)
        if min_ops != 10**9 + 1:
            return min_ops
        else:
            return -1



print(Solution().minOperations([1, 1, 4, 2, 3], 5))
# print(Solution().minOperations([5, 6, 7, 8, 9], 4))
