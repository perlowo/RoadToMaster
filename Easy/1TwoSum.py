from typing import List

class SomeClass:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and (nums[i] + nums[j] == target) and not d:
                    d.append(i)
                    d.append(j)
        return d

# Create an instance of SomeClass
obj = SomeClass()

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = obj.twoSum(nums, target)

print(result)  # Print the result
