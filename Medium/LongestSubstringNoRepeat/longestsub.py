class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_length = 0
        start = 0
        chars_index = {}

        for end, char in enumerate(s):
            if char in chars_index and start <= chars_index[char]:
                start = chars_index[char] + 1
            else:
                max_length = max(max_length, end - start + 1)

            chars_index[char] = end

        return start + max_length

