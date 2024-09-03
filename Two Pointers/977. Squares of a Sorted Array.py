class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # Get the length of the list 'nums' and store it in a variable 'n'.
        n = len(nums)
        
        # Initialize two pointers 'l' for the beginning of the list, 'r' for the end of the list 
        l, r = 0, n - 1
        
        # Initialize an empty list called 'res' to store the squared numbers.
        res = []

        # Loop through each index 'i' in the list 'nums' to square each number in 'nums'
        for i in range(n): 
            # Square the number at index 'i' and store the result back in 'nums' at the same index.
            nums[i] = nums[i] ** 2
        
        # Sort the squared numbers into the 'res' list in non-decreasing order using a two-pointer approach 
        while l <= r: 
            # Compare the squared numbers at the 'l' and 'r' pointers.
            if nums[l] < nums[r]:
                # If the number at 'r' is greater than the number at 'l' append the number at 'r' to the 'res' list.
                res.append(nums[r])
                
                # Move the 'r' pointer one step to the left (decrease its index by 1).
                r -= 1
            else:
                # If the number at 'l' is greater than or equal to the number at 'r' append the number at 'l' to the 'res' list.
                res.append(nums[l])
                
                # Move the 'l' pointer one step to the right (increase its index by 1).
                l += 1

        # The 'res' list is currently in decreasing order, so we need to reverse it to make it non-decreasing.
        res.reverse()

        # Return the final sorted list of squared numbers.
        return res
