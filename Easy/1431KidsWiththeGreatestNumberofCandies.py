class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        target = 0
        for i in range(len(candies)):
            if candies[i] > target:
                target = candies[i]
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= target:
                result.append(True)
            else:
                result.append(False)
        return result