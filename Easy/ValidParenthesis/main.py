
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        charset = s.strip()
        stack = []
        for i in charset:
            print(i)

            if len(stack) == 0:
                stack.append(i)
                continue

            if i == "(" or i == "{" or i == "[":
                stack.append(i)
                continue
            elif i == "(" and stack[len(stack) - 1] in ["{", "["]:
                print(stack[len(stack) - 1])
                return False
            elif i == "{" and stack[len(stack) - 1] in ["(", "["]:
                return False
            elif i == "[" and stack[len(stack) - 1] in ["{", "("]:
                return False
            elif i == ")" and stack[len(stack) - 1] in ["{", "["]:
                print(stack[len(stack) - 1])
                return False
            elif i == "}" and stack[len(stack) - 1] in ["(", "["]:
                return False
            elif i == "]" and stack[len(stack) - 1] in ["{", "("]:
                return False
            elif i == ")" and stack[len(stack) - 1] == "(" or i == "}" and stack[len(stack) - 1] == "{" or i == "]" and stack[len(stack) - 1] == "[":
                stack.pop()

        if len(stack) != 0:
            return False
        else:
            return True


with open("test.txt", "r") as f:
    s = Solution()
    for _ in f.readlines():
        print(s.isValid(_))