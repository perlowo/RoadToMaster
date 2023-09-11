from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        output = []
        for i in range(len(nums)):
            if nums[i] != val:
                output.append(nums[i])
            else:
                pass
        k = len(output)
        # print(output)
        nums.clear()
        nums.extend(output)
        return k

num = [0,1,2,2,3,0,4,2]
print(Solution().removeElement(num, 2))