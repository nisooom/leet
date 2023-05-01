class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]

        """
        listSTRS: list = strs

        anagrams = []
        for i in listSTRS:
            tmp = [i]
            for j in strs:
                if i == j:
                    continue
                letterset = set(i)
                isAnagram = True
                for k in j.strip(''):
                    if k == "":
                        pass
                    if k not in letterset:
                        isAnagram = False
                        break

                if isAnagram:
                    tmp.append(j)
                    listSTRS.remove(j)

            anagrams.append(tmp)

        return anagrams

if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))