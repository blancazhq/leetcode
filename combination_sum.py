class Solution(object):
    def combinationSum(self, candidates, target):
      """
      :type candidates: List[int]
      :type target: int
      :rtype: List[List[int]]
      """
      finalResults = []
      candidates.sort()
      length = len(candidates)

      for i in range(0, len(candidates)):
        results1 = self.findCombination(candidates[length-i-1:length], target, [], 0)
        if results1 and results1 not in finalResults:
          finalResults.append(results1)
        results2 = self.findCombination(candidates[0:i+1], target, [], 0)
        if results2 and results2 not in finalResults:
          finalResults.append(results2)

      return finalResults

    def findCombination(self, candidates, target, results, sum):
      sum += candidates[0]
      results.append(candidates[0])
      if target == sum:
        return results
      elif target < sum:
        results = []
        return results
      if len(candidates) >= 1:
        if (len(candidates) > 1 and target - sum > candidates[0] and target - sum <= candidates[1]):
          candidates.pop(0)          
        return self.findCombination(candidates, target, results, sum)

solution = Solution()

print solution.combinationSum([2, 1, 5, 7], 6)

[2, 3, 6, 7]