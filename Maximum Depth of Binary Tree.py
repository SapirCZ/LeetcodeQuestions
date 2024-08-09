# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_length = 0

    def depth_first_search_inOrder(self, node, depth):
        if node.left:
            self.depth_first_search_inOrder(node.left, depth)
        depth.append(node.data)
        if node.right:
            self.depth_first_search_inOrder(node.right, depth)
        return depth
