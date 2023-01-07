class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        step = 0
        while num > 0:
            step += 1
            if num % 2 == 0:
                num = int(num/2)
            else:
                num -= 1
        return step

if __name__ == '__main__':
    ns = Solution()

    print(ns.numberOfSteps(14))
