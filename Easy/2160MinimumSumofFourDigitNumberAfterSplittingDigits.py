class Solution:
    def minimumSum(self, num: int) -> int:
        digits = str(num)
        smallnum1 = digits[0]
        smallnum1index = 0
        smallnum2 = 10
        smallnum2index = 0
        bignum1 = digits[0]
        bignum1index = 0
        bignum2 = digits[0]
        j = 0

        for j in range(len(digits)):
            if(digits[j] == "0"):
                smallnum1 = 0
                print(j)
            if (int(digits[j]) > 0) and (int(smallnum1) > int(digits[j])):
                smallnum1 = digits[j]
                smallnum1index = j
                print(j)

        for i in range(len(digits)):
            if(digits[i] == "0" and smallnum1index != i):
                smallnum2 = 0
                print(i)
            if ((int(digits[i]) > 0) and (int(smallnum2) > int(digits[i])) and smallnum1index != i):
                smallnum2 = digits[i]
                smallnum2index = i
                print(i)

        for j in range(len(digits)):
            if ((int(digits[j]) > 0) and (int(bignum1) < int(digits[j])) and smallnum1index != j and smallnum2index != j):
                bignum1 = digits[j]
                bignum1index = j
                print(j)

        for i in range(len(digits)):
            print("shit11111")
            if int(digits[i]) > 0 and i != bignum1index and i != smallnum1index and i != smallnum2index:
                print("shit")
                bignum2 = digits[i]
            else:
                bignum2 = 0

        number1 = []
        number2 = []
        number1.append(smallnum1)
        number2.append(smallnum2)
        # print(bignum2)
        if int(bignum1) > int(bignum2):
            number1.append(bignum1)
            number2.append(bignum2)
        else:
            number1.append(bignum2)
            number2.append(bignum1)
        number1 = [int(i) for i in number1]
        number2 = [int(i) for i in number2]

        new_list = [str(current_integer) for current_integer in number1]
        string_value = "".join(new_list)
        numbero1 = int(string_value)
        print(numbero1)
        new_list = [str(current_integer) for current_integer in number2]
        string_value = "".join(new_list)
        numbero2 = int(string_value)
        print((numbero2))

        return numbero1 + numbero2


print(Solution().minimumSum(3009))
