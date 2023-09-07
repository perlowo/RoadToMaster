from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_num = []

        while x > 0:
            digit = x % 10
            list_num.insert(0, digit) 
            x //= 10

        for i in range(len(list_num)):
            if list_num[i] != list_num[-i-1]:
                return False

        return True

obj = Solution()
result = obj.isPalindrome(12321)
print(result)