class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict = {item1: idx for idx, item1 in enumerate(list1)}
        best = 2000
        answer = []

        for idx, item2 in enumerate(list2):
            if idx + dict.get(item2, 2000)<best:
                print "best1", best
                best = idx + dict.get(item2, 2000)
                print "best2", best
                answer = [item2]
            elif idx + dict.get(item2, 2000)==best:
                answer.append(item2)

        return answer



solution = Solution()

print solution.findRestaurant(["KFC", "Burger King", "Tapioca Express", "Shogun"],
["KFC", "Shogun", "Burger King"])
