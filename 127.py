class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        def is_neighbor(word1,word2):
            total_difference=0
            for i in range(len(word1)):
                difference=abs(ord(word1[i])-ord(word2[i]))
                if difference!=0:
                    total_difference+=1
            return True if total_difference==1 else False

        def bfs(start_word,end_word):
            visited=set()
            queue=deque([(start_word,1)])
            while queue:
                word,step_length=queue.popleft()
                #do something here

                if word==end_word:
                    return step_length

                if word not in visited:
                    visited.add(word)
                    for choice_word in wordList:
                        if is_neighbor(choice_word,word):
                            queue.append((choice_word,step_length+1))

            return 0

        return bfs(beginWord,endWord)