class Solution:
    def subtractProductAndSum(self, n):
        # Convert the integer to a string to extract digits
        digits = str(n)
        print(digits)
        # Initialize variables to calculate product and sum
        product = 1
        digit_sum = 0
        
        # Calculate product and sum of digits
        for digit in digits:
            digit_int = int(digit)
            print(digit_int)
            product *= digit_int
            digit_sum += digit_int
        
        # Calculate the difference between product and sum
        result = product - digit_sum
        
        return result

print(Solution().subtractProductAndSum(234))   # Output: 15
print(Solution().subtractProductAndSum(4421))  # Output: 21