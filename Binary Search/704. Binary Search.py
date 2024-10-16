class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) # Get length of array 
        l = 0 # Initalize left pointer
        r = n - 1 # Initalize right pointer 

        while l <= r: 
            m = l + ((r-l) //2) # Get the middle index of left and right pointers

            if nums[m] == target: # If middle index = target return middle index
                return m # Return True (m)
            elif target < nums[m]: # If middle index > target move right pointer left of m
                r = m - 1
            else: 
                l = m + 1 # middle index < target move left pointer to right of middle index

        return -1 # Return false(-1)
        
