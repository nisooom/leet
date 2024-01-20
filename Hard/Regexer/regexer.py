import re


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        while p.find("**") != -1:
            p = p.replace("**", "*")

        matches = re.findall(p, s)
        if len(matches) >= 1:
            if len(matches[0]) == len(s):
                return True

        return False
