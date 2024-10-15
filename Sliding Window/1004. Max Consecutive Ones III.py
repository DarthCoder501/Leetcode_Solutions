class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums) # Get the length of the array 
        longest = 0 # Set the consecutive 1's length 
        l = 0 # Set left pointer to 0 
        numZeros = 0  # Count the number of zeros that appear 

        # Loops thorugh each element in array 
        for r in range(n):
            # If element at that index = 0 increase zeros count by 1 
            if nums[r] == 0:
                numZeros += 1 
            # While the count of zeros is more than K move left pointer 
            while numZeros > k:
                # If the element at that index = 0 decrease the zeros count by 1 
                if nums[l] == 0: 
                    numZeros -= 1
                # Move the left pointer otherwise 
                l += 1 

            w = r - l + 1  # Get the length of the window 
            longest = max(longest, w) # Get the biggest window so far 

        return longest # Return the biggest window found
