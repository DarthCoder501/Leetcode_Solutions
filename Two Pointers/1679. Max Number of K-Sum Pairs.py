class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs = 0 # count nums of pairs 
        l, r  = 0, len(nums) - 1 # initalize the pointers 
        s = sorted(nums) # sort the nums list 

        while l < r: 
            if s[l] + s[r] == k: 
                pairs += 1 # increment pair count by 1 
                l += 1 # move both pointers closer to the middle 
                r -= 1 
            elif s[l] + s[r] < k: 
                l += 1 # sum too small so move l 
            else: 
                r-= 1 # sum too large so move r 

        return pairs # return the pairs count 
