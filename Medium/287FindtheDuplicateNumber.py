from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen_numbers = set()
        for num in nums:
            if num in seen_numbers:
                return num
            else:
                seen_numbers.add(num)



print(Solution().findDuplicate([1, 3, 4, 2, 2]))
