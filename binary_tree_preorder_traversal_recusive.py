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

        def preorderTraversalRecur(root, result):
            if root:
                result.append(root.val)
                preorderTraversalRecur(root.left, result)
                preorderTraversalRecur(root.right, result)
        
        preorderTraversalRecur(root, result)
        
        return result

solution = Solution()

myTree = TreeNode(1)
myTree.left = TreeNode(2)
myTree.right = TreeNode(3)
myTree.left.left = TreeNode(4)
myTree.left.right = TreeNode(5)

print solution.preorderTraversal(myTree)