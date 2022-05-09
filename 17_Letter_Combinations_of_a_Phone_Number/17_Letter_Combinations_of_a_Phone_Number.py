class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        dic1 = {
            1:[""],
            2:["a", "b", "c"],
            3:["d", "e", "f"],
            4:["g", "h", "i"],
            5:["j", "k", "l"],
            6:["m", "n", "o"],
            7:["p", "q", "r", "s"],
            8:["t", "u", "v"],
            9:["w", "x", "y", "z"]
        }
        allKeypad = []
        for j in digits:
            allKeypad.append(dic1[int(j)])
        
        current = ""
        allCombi = []
        moreDigit(0, allKeypad, current, allCombi)
        return allCombi
        
                
                
def moreDigit(index, allKeypad, current, allCombi):
    if len(allKeypad) == 0:
        return 
    
    if index == len(allKeypad):
        allCombi.append(current)
        return
        
    for n in allKeypad[index]:
        moreDigit(index+1, allKeypad, current + n,allCombi)
        
    
        
            
            
        