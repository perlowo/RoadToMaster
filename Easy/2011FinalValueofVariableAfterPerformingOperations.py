class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        j = 0
        for i in range(len(operations)):
            if operations[i-1] == "X++":
                j+=1
            if operations[i-1] == "++X":
                j+=1
            if operations[i-1] == "--X":
                j-=1
            if operations[i-1] == "X--":
                j-=1
        return j