class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = {}
        ops = 0
        
        for i in nums:
            if i < k:
                if i in counter:
                    counter[i] += 1
            
                else:
                    counter[i] = 1
    
        for j in counter:
            if (k - j) in counter:
                if counter[j] > counter[k - j]:
                    ops += counter[k-j]
            
                else:
                    ops += counter[j]
    
        return ops/2

        