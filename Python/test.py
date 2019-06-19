class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insetleft(self, value):
        self.left = TreeNode(value)
        self.left.parent = self
        return self.left

    def insertright(self, value):
        self.right = TreeNode(value)
        self.right.parent = self
        return self.right

    def show(self):
        print(self.data)
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:#递归边界
            return 0
        else:
            l=1+self.maxDepth(root.left)#递归
            r=1+self.maxDepth(root.right)
            return max(l,r)
solution = Solution()
root = TreeNode(3)
a = root.insertleft(9)
b = root.insertright(20)
c = a.insertleft(None)
d = a.insertright(None)
e = b.insertleft(15)
f = b.insertright(7)
print(solution.maxDepth(root))
