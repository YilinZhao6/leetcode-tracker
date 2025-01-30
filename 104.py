class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        depths=[]
        def dfs(node,depth):
            #encounters a leaf
            if not node:
                depths.append(depth)
                return

            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        
        dfs(root,0)
        
        return max(depths)