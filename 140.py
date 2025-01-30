class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s:
            return []

        result=[]

        def backtrack(letters,selected_words,result):
            if not letters:
                res=reversed(selected_words)
                result.append(' '.join(res))
            
            for i in range(len(wordDict)):
                dict_word_length=len(wordDict[i])
                n=len(letters)
                if wordDict[i]==letters[n-dict_word_length:]:
                    selected_words.append(wordDict[i])
                    backtrack(letters[:n-dict_word_length],selected_words,result)
                    #pop off the choices
                    selected_words.pop()

        #call the main function
        backtrack(s,[],result)


        return result

