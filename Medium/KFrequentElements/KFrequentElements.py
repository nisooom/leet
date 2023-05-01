class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numdict: dict = {}

        for i in nums:
            if i in numdict.keys():
                numdict[i] += 1
            else:
                numdict[i] = 1

        sortedDict = sorted(numdict.items(), key=lambda kv: (kv[1], kv[0]))

        sortedKeys = [i for (i,j) in sortedDict]



if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))