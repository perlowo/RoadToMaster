class Solution:
    def romanToInt(s: str) -> int:
        roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    
        result = 0
        prev_value = 0

        for char in s[::-1]:
            print(char)
            value = roman_values[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result

print(Solution.romanToInt("MCMXCIV"))