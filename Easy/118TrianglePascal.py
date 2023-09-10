from typing import List

class Solution:
    
    def gen(self,rows_n):
        ans = [[1]]
        for _ in range(1,rows_n):
            n = len(ans[-1])
            ans.append(
                [
                ans[-1][i-1] + ans[-1][i] if i and i < n else 1
                for i in range(n+1)
                ]
            )
        return ans 

s = Solution()
result = s.gen(5)
print(result)

    
'''
output = [] 
for i in range(iles tam):
    if cos:
        output.append(True)
    else:
        output.append(False)

== 


output = [ 
    True if cos true else False 
    for i in range(iles tam)
]

output = [ True if cos true else False for i in range(iles tam)]


'''

'''
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for _ in range(1,numRows):
            floor = output[-1]
            new_floor = []
            length = len(floor)
            for j in range(length+1):
                if j and j < length:
                   new_floor.append( floor[j-1] + floor[j])
                else:
                    new_floor.append(1)
            output.append(new_floor)
        return output
    '''