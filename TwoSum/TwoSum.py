class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             pass
        #         else:
        #             if nums[i] + nums[j] == target:
        #                 return [i, j]

        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: return [d[r], i]
            d[j] = i

if __name__ == '__main__':
    twosum = Solution().twoSum([3, 2, 4], 6)
    print(twosum)
