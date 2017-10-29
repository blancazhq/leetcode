# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []

        if root is not None:
          stack.append(root)
          while len(stack) > 0:
            result.append(stack[-1].val)
            node = stack.pop()
            if node.right is not None:    
              stack.append(node.right)
            if node.left is not None:
              stack.append(node.left)
            
        return result

solution = Solution()

myTree = TreeNode(1)
myTree.left = TreeNode(2)
myTree.right = TreeNode(3)
myTree.left.left = TreeNode(4)
myTree.left.right = TreeNode(5)

print solution.preorderTraversal(myTree)