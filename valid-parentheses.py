class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if stack and stack[-1] == dict.get(char, None):
                del stack[-1]
            else:
                stack.append(char)

        return len(stack) == 0


solution = Solution()

print solution.isValid("([)]")
