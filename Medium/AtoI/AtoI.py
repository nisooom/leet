import re


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip().split(" ")

        if len(s) >= 1:

            try:
                test_num = s[0]
                try:
                    ans = int(test_num)
                    min_val = -2147483648
                    max_val = 2147483647
                    print("here")
                    if min_val > ans:
                        return min_val
                    elif ans > max_val:
                        return max_val
                    else:
                        return ans

                except ValueError:
                    pass

                try:
                    ans = test_num.split(".")
                    if len(ans) == 2:
                        min_val = -2147483648
                        max_val = 2147483647
                        print("here")
                        if min_val > ans:
                            return min_val
                        elif ans > max_val:
                            return max_val
                        else:
                            return ans

                except ValueError:
                    pass

            except Exception:
                pass

            #
            # match = re.findall(r'[+-]?\d+\b[(.\d+)]?\b', s[0])
            # print(match)
            # if len(match) == 1:
            #     print(match[0])

        return 0
