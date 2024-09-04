class Solution:
    # Define a method that takes in a list of integers: nums
    def findClosestNumber(self, nums: List[int]) -> int:
        # Get the length of the nums list
        i = len(nums)
        # Initialize the variable 'closest' with the first element of the list
        closest = nums[0]
        
        # Loop through each element in the list nums
        for j in range(i):
            # Calculate the absolute value of the current element nums[j]
            h = abs(nums[j])
            
            # If the absolute value of the current element is less than the absolute value of 'closest'
            if abs(nums[j]) < abs(closest):
                # Update 'closest' to the current element since it's closer to 0
                closest = nums[j]
            # If the absolute value of the current element equals the absolute value of 'closest'
            elif abs(nums[j]) == abs(closest):
                # Check if the current element is greater than 'closest'
                if nums[j] > closest: 
                    # Update 'closest' to the current element if it is greater
                    closest = nums[j]
                    
        # Return the element that is closest to zero
        return closest
