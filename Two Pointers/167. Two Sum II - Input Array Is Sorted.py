class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Initialize two pointers, 'l' and 'r', 'l' to start at the beginning of the lest and 'r' to start the end
        l = 0 
        r = len(numbers) - 1

        # While loop that continues as long as 'l' is less than 'r'. 
        while l < r: 
            
            # If the sum of the numbers at 'l' and 'r' greater than target, need a smaller sum, move 'r' one step to the left.
            if numbers[l] + numbers[r] > target: 
                r -= 1
            
            #If the sum of the numbers at 'l' and 'r' smaller than target, need a larger sum, move 'l' one step to the right.  
            elif numbers[l] + numbers[r] < target:
                l += 1
            
            # If the sum of the numbers at 'l' and 'r' equals the target, found the numbers we're looking for.
            else: 
                return [l + 1, r + 1] # Since the problem expects a 1-based index (not 0-based), we return [l+1, r+1].
