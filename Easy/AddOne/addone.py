class Solution:
    def plusOne(self, digits):
        x = int("".join([i for i in digits])) + 1
        return [int(i) for i in str(x)]
