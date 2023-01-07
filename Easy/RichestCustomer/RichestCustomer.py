class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        total = []
        for i in accounts:
            total.append(sum([j for j in i]))

        return max(total)
