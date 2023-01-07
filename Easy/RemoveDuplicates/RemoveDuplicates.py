class Solution(object):
    def removeDuplicates(self, nums):
        num_dict = {}
        for i in nums:
            if i in num_dict.keys():
                num_dict[i] += 1
            else:
                num_dict[i] = 1

        sorted_arr = [i for i in num_dict.keys()]
        # for i in range(len(nums) - len(sorted_arr)):
        #     sorted_arr.append("_")

        return len(sorted_arr)
