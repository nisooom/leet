import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        x = len(nums1)
        y = len(nums2)

        mixed = []

        i = 0
        j = 0

        while i < x and j < y:

            if nums1[i] < nums2[j]:
                mixed.append(nums1[i])
                i += 1
            else:
                mixed.append(nums2[j])
                j += 1

        while i < x:
            mixed.append(nums1[i])
            i += 1

        while j < y:
            mixed.append(nums2[j])
            j += 1

        med = 0
        if len(mixed) % 2 == 0:
            x = int(len(mixed)/2)
            med = float((mixed[x] + mixed[x+1])/2)
        else:
            x = math.ceil(len(mixed)/2)
            med = float((mixed[x]/ 2))

        return med
