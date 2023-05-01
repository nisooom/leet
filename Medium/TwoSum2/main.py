class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
        """

        left_index = 0
        right_index = len(numbers) - 1

        while left_index < right_index:
            current_sum = numbers[left_index] + numbers[right_index]

            if current_sum == target:
                return [left_index + 1,right_index + 1]
            elif current_sum > target:
                right_index -= 1
            else:
                left_index += 1



if __name__ == '__main__':
    sol = Solution()
    sol.twoSum([2,7,11,15], 9)