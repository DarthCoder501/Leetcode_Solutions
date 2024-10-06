class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0 # # initialize left pointer to track position for non-zero elements
        n = len(nums) # store list length as variable 

        for r in range(n): # iterate over each element in the list with right pointer
            if nums[l] == 0 and nums[r] != 0: # check if swap is possible 
                nums[l], nums[r] = nums[r], nums[l] # swap zero with non zero 
                l += 1 # move left pointer forwards 
            if nums[l] != 0: # if number is non zero 
                l += 1 # move left pointer forward
