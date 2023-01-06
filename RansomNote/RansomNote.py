import re

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNoteDict = {}
        magazineDict = {}

        for c in ransomNote:
            if c not in ransomNoteDict:
                ransomNoteDict[c] = 1
            else:
                ransomNoteDict[c] += 1

        for c in magazine:
            if c not in magazineDict:
                magazineDict[c] = 1
            else:
                magazineDict[c] += 1
        return magazineDict == ransomNoteDict