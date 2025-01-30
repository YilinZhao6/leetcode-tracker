class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        depths=[]
        def dfs(node,depth,returnable):
            #encounters a leaf
            if not node:
                if returnable:
                    depths.append(depth)
                return
            
            if node.left is None and node.right is None:
                dfs(node.left,depth+1,True)
                dfs(node.right,depth+1,True)
            else:
                dfs(node.left,depth+1,False)
                dfs(node.right,depth+1,False)
        
        dfs(root,0,False)

        
        return min(depths)