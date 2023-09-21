class Solution:
    def countMatches(items, ruleKey, ruleValue):
        count = 0
        
        key_indices = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        
        for item in items:
            if item[key_indices[ruleKey]] == ruleValue:
                count += 1
        
        return count
