# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
#
# Note:
# Each element in the result must be unique.
# The result can be in any order.

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []

        for num in nums2:
            if num in nums1 and num not in intersection:
                intersection.append(num)

        return intersection

solution = Solution();
print solution.intersection([1, 2, 2, 1],[2, 2]);
