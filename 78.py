class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        #the graph is already created so we don't need another one.

        if not graph:
            return []

        end_node=len(graph)-1
        paths=[]

        def dfs(graph,node,path):
            if node==end_node:
                path.append(node)
                paths.append(path[:])
                return

            path.append(node)
            for neighbor in graph[node]:
                dfs(graph, neighbor, path[:])

        dfs(graph,0,[])
        
        return paths

