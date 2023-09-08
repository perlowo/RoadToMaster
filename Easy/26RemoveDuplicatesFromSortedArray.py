class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        j = 0
        numscorrect = [0]
        for i in range(0, len(nums)):
            print(i)
            if nums[i] != nums[i-1] and (i > 0):
                print(numscorrect[j])
                if numscorrect[j] != nums[i]:
                    numscorrect.append(nums[i])
                    print("numscorrect")
                    j += 1
                    k += 1
                else:
                    pass
            elif i == 0:
                numscorrect.append(nums[i])
                numscorrect.pop(0)
            else:
                pass

        # print(numscorrect)
        nums.clear()
        nums.extend(numscorrect)
        # print(nums)