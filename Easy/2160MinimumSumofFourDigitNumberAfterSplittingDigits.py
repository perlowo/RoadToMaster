# class Solution:
    # def minimumSum(self, num: int) -> int:
    #     digits = str(num)
    #     smallnum1 = digits[0]
    #     smallnum1index = 0
    #     smallnum2 = 10
    #     smallnum2index = 0
    #     bignum1 = digits[0]
    #     bignum1index = 0
    #     bignum2 = digits[0]

    #     for j in range(len(digits)):
    #         if(digits[j] == "0"):
    #             smallnum1 = 0
    #             smallnum1index = j
    #         if (int(digits[j]) > 0) and (int(smallnum1) > int(digits[j])):
    #             smallnum1 = digits[j]
    #             smallnum1index = j

    #     for i in range(len(digits)):
    #         if(digits[i] == "0" and smallnum1index != i):
    #             smallnum2 = 0
    #             smallnum2index = i
    #         if ((int(digits[i]) > 0) and (int(smallnum2) > int(digits[i])) and smallnum1index != i):
    #             smallnum2 = digits[i]
    #             smallnum2index = i

    #     for j in range(len(digits)):
    #         if(digits[j] == "0" and smallnum1index != j and smallnum2index != j):
    #             smallnum2 = 0
    #             smallnum2index = i
    #         if ((int(digits[j]) > 0) and (int(bignum1) < int(digits[j])) and smallnum1index != j and smallnum2index != j):
    #             bignum1 = digits[j]
    #             bignum1index += j

    #     for i in range(len(digits)):
    #         print(f"bignum1index: {bignum1index}")
    #         print(f"smallnum2index: {smallnum2index}")
    #         print(f"smallnum1index: {smallnum1index}")
    #         if (i != bignum1index-1) and (i != smallnum1index) and (i != smallnum2index):
    #             bignum2 = int(digits[i])
    #             if (i != bignum1index-1) and (i != smallnum1index) and (i != smallnum2index):
    #                 bignum2 = int(digits[i])

    #     number1 = []
    #     number2 = []
    #     number1.append(smallnum1)
    #     number2.append(smallnum2)
    #     # print(bignum2)
    #     if int(bignum1) > int(bignum2):
    #         number1.append(bignum1)
    #         number2.append(bignum2)
    #     else:
    #         number1.append(bignum2)
    #         number2.append(bignum1)
    #     number1 = [int(i) for i in number1]
    #     number2 = [int(i) for i in number2]

    #     new_list = [str(current_integer) for current_integer in number1]
    #     string_value = "".join(new_list)
    #     numbero1 = int(string_value)
    #     print(numbero1)
    #     new_list = [str(current_integer) for current_integer in number2]
    #     string_value = "".join(new_list)
    #     numbero2 = int(string_value)
    #     print((numbero2))

    #     return numbero1 + numbero2

class Solution:
    def minimumSum(self, num: int) -> int:
        num = [ int(c) for c in sorted(str(num),reverse=True) ]
        return num.pop() * 10 + num.pop() * 10 + num.pop() + num.pop()



print(Solution().minimumSum(2436))
print(Solution().minimumSum(4009))
