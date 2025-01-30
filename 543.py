# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.diameter=0

        def dfs_find_depth(node):
            if not node:
                return 0
            
            left_depth=dfs_find_depth(node.left)
            right_depth=dfs_find_depth(node.right)

            self.diameter=max(self.diameter,left_depth+right_depth)

            return max(left_depth,right_depth)+1
        
        dfs_find_depth(root)
        return self.diameter