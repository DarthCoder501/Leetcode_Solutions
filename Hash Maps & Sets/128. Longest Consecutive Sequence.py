class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Convert the list 'nums' into a set called 's'. 
        s = set(nums)
        
        # Initialize a variable 'longest_cons' to 0 which will track of the length of the longest consecutive sequence found so far.
        longest_cons = 0 
        
        # Loop through each number in the original list 'nums'.
        for num in nums: 
            
            # Check if 'num - 1' (the number just before 'num') is not in the set 's' to identify the start of a new consecutive sequence.
            if num - 1 not in s: 
                # Initialize a variable 'nextnum' to 'num + 1' to check for the next number in the sequence.
                nextnum = num + 1
                
                # Initialize a variable 'cons_length' to 1 to track of the length of the current consecutive sequence.
                cons_length = 1 
                
                # While loop to keep checking if 'nextnum' is in the set 's', If it is increment 'cons_length' & move to the next number.
                while nextnum in s: 
                    
                    # Increment the length of the current sequence.
                    cons_length += 1 
                    
                    # Move to the next number in the sequence by incrementing 'nextnum'.
                    nextnum += 1
                
                # After exiting while loop, update 'longest_cons' w/ maximum value between the current longest sequence & the one just found.
                longest_cons = max(longest_cons, cons_length)

        # Return the length of the longest consecutive sequence found in the list.
        return longest_cons
