class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odds = []
        even = []
        for i in nums:
            if i%2 == 0:
                even.append(i)
            
            else:
                odds.append(i)
                
        return even + odds
        