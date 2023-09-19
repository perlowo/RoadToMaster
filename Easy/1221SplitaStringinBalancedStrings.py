class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "L":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
            print(balance)
        return count