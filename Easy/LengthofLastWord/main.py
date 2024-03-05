class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr_new = [i if i != " " else False for i in s.split(" ")]

        for i in range(len(arr_new) - 1, -1, -1):
            if arr_new[i]:
                print(arr_new[i])
                return len(arr_new[i])

# Hi