class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort the array to use two pointer appraoch easier 
        n = len(nums) # get size of nums array 
        res = [] #store the triplets 
        
        for i in range(n): #iterate through each index of array 
            if nums[i] > 0: #if num is pos next nums will be greater nums not possibe for triplet = 0
                break 
            elif i > 0 and nums[i] == nums[i-1]: #check if we alr solved triplet to avoid duplicate
                continue #moves onto next num  
            
            l, r = i + 1, n - 1 #set pointers 
            while l < r: 
                sums = nums[i] + nums[l] + nums[r]
                if sums == 0: 
                    res.append([nums[i], nums[l], nums[r]]) #add triplet
                    l, r = l + 1, r - 1 #move left and right pointers 
                    while l < r and nums[l] == nums[l-1]: #move l pointer to avoid using same nums[l]
                        l+= 1
                    while l < r and nums[r] == nums[r+1]: #move r pointer to avoid using same nums[r]
                        r -= 1    
                elif sums > 0: #move r pointer if value too high 
                    r -= 1
                else: #move l pointer if value too low 
                    l += 1 
        return res 
