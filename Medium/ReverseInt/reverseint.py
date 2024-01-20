import re


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        x_str = str(x)
        reversed_str = ""

        x_list = re.findall(r'\d', x_str)

        if x_str[0] == "-":
            reversed_str += "-"

        if x_list[-1] == "0":
            x_list.pop()

        reversed_str += "".join(x_list[::-1])

        if reversed_str == "":
            return 0

        ans = int(reversed_str)

        min_val = -2_147_483_648
        max_val = 2_147_483_647

        if min_val <= ans <= max_val:
            return ans
        else:
            return 0