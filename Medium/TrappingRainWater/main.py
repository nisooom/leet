class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
        """

        h = max(height) + 1

        numMap = []

        for i in range(0, h):
            tmp = []
            for j in range(0, len(height)):
                val = height[j]
                if val == h-i:
                    tmp.append(1)
                else:
                    tmp.append(0)

            numMap.append(tmp)

        for i in range(0, h - 1):
            for j in range(0, len(height)):
                if numMap[i][j] == 1:
                    for k in range(i, h):
                        numMap[k][j] = 1

        # for i in range(0, h -1):
        #     for j in range(0, len(height)):

        spaces = []

        for i in numMap:
            counter = 0
            start = None
            end = None
            for (k,l) in enumerate(i):
                if l == 1:
                    if counter == 0:
                        counter += 1
                        start = k
                    if counter == 1:
                        end = k
            print(counter)
            print(start)
            print(end)



        for i in numMap:
            print(i)


if __name__ == '__main__':
    sol = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])