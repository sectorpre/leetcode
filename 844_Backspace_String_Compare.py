def codeclean(s):
    """
    cleans the first backspace key in a list and calls itself again.
    returns if there are no more backspace keys
    """
    check = 0
    rs = s
    for i in range(len(s)):
            if (s[i] == "#"):
                rs[i] = "0"
                if (i != 0):
                    rs[i-1] = "0"
                check = 1
                break
    
    #if all backspaces have not been cleaned yet
    if check == 1:
        rs = codeclean([i for i in rs if i != "0"])
        
    return rs
                
    

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if codeclean(list(s)) == codeclean(list(t)):
            return True
        
        return False
        