"""
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def inorder(self):
        if self.val:
            if self.left:
                self.left.inorder()
            print(self.val)
            if self.right:
                self.right.inorder()


def array_to_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    node.left = array_to_bst(nums[:mid])
    node.right = array_to_bst(nums[mid + 1:])
    return node

def hasPathSum(root: TreeNode, sum: int)-> bool:
    if not root:
        return False
    sum -= root.val
    if root.left is None and root.right is None:
        return sum == 0
    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)

nums = [1, 2, 3, 4, 5, 6]

n = array_to_bst(nums)
print(TreeNode.inorder(n))

print(hasPathSum(n, 22))
