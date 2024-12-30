class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        s_list=list(s)
        pt1=0
        pt2=len(s_list)-1
        jumped=False

        while pt1<=pt2:
            if s_list[pt1]==s_list[pt2]:
                pt1+=1
                pt2-=1
            else:
                if jumped:
                    return False

                #jump one on left
                pt1+=1
                if s_list[pt1]==s_list[pt2]:
                    jumped=True
                else:
                    pt1-=1
                    #jump one on right
                    pt2-=1
                    if s_list[pt1]==s_list[pt2]:
                        jumped=True
                    else:
                        return False

        return True