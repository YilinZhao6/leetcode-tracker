from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        wordList.append(beginWord)
        #for each word in wordlist, find out who is neighbor
        def is_neighbor(word1,word2):
            m=len(word1)
            n=len(word2)
            if m!=n:
                return False
            total_difference=0
            for i in range(m):
                if word1[i]!=word2[i]:
                    total_difference+=1

            return True if total_difference==1 else False
        
        #appending neighbor to a dict
        neighbors=defaultdict(list)
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if is_neighbor(wordList[i],wordList[j]):
                    neighbors[wordList[i]].append(wordList[j])

        result = []
        
        # ✅ Your BFS Function (Adapted for Word Ladders)
        def bfs(start, target, path,visited=None):
            if visited==None:
                visited=set()
            
            if start==target:
                result.append(path[:])

            for neighbor in neighbors[start]:
                if neighbor not in visited:
                    path.append(neighbor)
                    visited.add(neighbor)
                    bfs(neighbor,target,path[:],visited)
                    path.pop()
                    visited.remove(neighbor)

    
        bfs(beginWord, endWord,[beginWord],set(beginWord))  # Call BFS with your function
        min_length=float('inf')
        for route in result:
            min_length=min(len(route),min_length)

        final_result=[]
        for route in result:
            if len(route)==min_length:
                final_result.append(route)

        return final_result
