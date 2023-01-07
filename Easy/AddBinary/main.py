class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # x = [int(i) for i in a]
        # y = [int(i) for i in b]

        res = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += ord(a[i]) - ord('0')
            if j >= 0:
                sum += ord(b[j]) - ord('0')
            i, j = i - 1, j - 1
            carry = 1 if sum > 1 else 0
            res += str(sum % 2)

        if carry != 0:
            res += str(carry)

        return res[::-1]

    #
    #     bin_sum = self.getBinSum(x, self.getBinSum(y, 0))
    #
    #     print(bin_sum)
    #
    #     bin_s = bin(bin_sum)
    #     return bin_s.replace("0b", "")
    #
    # def getBinSum(self, x, curr_sum):
    #     for i in range(len(x) - 1, -1, -1):
    #         if x[i] == 1:
    #             curr_sum += 2 ** (len(x) - i)
    #
    #     return curr_sum

    '----------'
    #     final_arr = []
    #     carry = 0
    #     if len(y) > len(x):
    #         for i in range(len(y) - 1, -1, -1):
    #             if x[i] + y[i] == 2:
    #                 carry = 1
    #                 final_arr.append(1)
    #             elif carry == 1:
    #                 final_arr.append()
    #                 carry = 0
    '------'


if __name__ == '__main__':
    x = Solution().addBinary("11", "1")
