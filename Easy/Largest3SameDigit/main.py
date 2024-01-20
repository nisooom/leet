class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """

        numDict = {}
        for i in num:
            if i in numDict.keys():
                numDict[i] += 1
            else:
                numDict[i] = 1

        finalDict = []
        for i in numDict.keys():
            if numDict[i] > 3:
                finalDict.append(int(i))

        print(numDict)
        print(finalDict)
        return f"{max(finalDict)}"*3


with open("test.txt", "r") as f:
    s = Solution()
    for _ in f.readlines():
        print(s.largestGoodInteger(_.strip()))